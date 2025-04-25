/* --------- Таблица ------------------------------------------------------- */
CREATE TABLE IF NOT EXISTS phonebook (
    id       SERIAL PRIMARY KEY,
    username TEXT    NOT NULL,
    phone    TEXT    NOT NULL
);

/* --------------------------------------------------------------- 1. Поиск */
CREATE OR REPLACE FUNCTION search_by_pattern(p_pattern TEXT)
RETURNS SETOF phonebook
LANGUAGE sql
AS $$
    SELECT * FROM phonebook
    WHERE username ILIKE '%' || p_pattern || '%'
       OR phone    ILIKE '%' || p_pattern || '%';
$$;

/* ----------------------------------------------------------- 2. Up‑sert 1 */
CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE phonebook
       SET phone = p_phone
     WHERE username = p_name;

    IF NOT FOUND THEN
        INSERT INTO phonebook(username, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$;

/* ----------------------------------------------- 3. Массовый up‑sert + валидация */
CREATE OR REPLACE PROCEDURE bulk_insert_users(
        p_names   TEXT[],
        p_phones  TEXT[],
        OUT bad_rows TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INTEGER;
BEGIN
    bad_rows := ARRAY[]::TEXT[];

    FOR i IN 1 .. array_length(p_names, 1) LOOP
        IF p_phones[i] !~ '^\d{10}$' THEN           -- телефон ≠ 10 цифр
            bad_rows := array_append(
                           bad_rows,
                           format('%s — %s', p_names[i], p_phones[i])
                        );
        ELSE
            CALL insert_or_update_user(p_names[i], p_phones[i]);
        END IF;
    END LOOP;
END;
$$;

/* ------------------------------------------------------------- 4. Удаление */
CREATE OR REPLACE PROCEDURE delete_user_by_value(p_value TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE username = p_value
       OR phone    = p_value;
END;
$$;

/* ------------------------------------------------------------- 5. Пагинация */
CREATE OR REPLACE FUNCTION get_page(p_limit INT, p_offset INT)
RETURNS SETOF phonebook
LANGUAGE sql
AS $$
    SELECT * FROM phonebook
    ORDER BY username
    LIMIT  p_limit
    OFFSET p_offset;
$$;

/* ------------ Проверочные вызовы (можно закомментировать) --------------- */
/*
-- одиночный upsert
CALL insert_or_update_user('Ann', '7777777777');

-- массовый upsert (один номер «битый» для теста)
CALL bulk_insert_users( ARRAY['Ben','Cat','Dog'],
                        ARRAY['1234567890','99','1112223333'],
                        NULL );

-- поиск по шаблону
SELECT * FROM search_by_pattern('7');

-- пагинация (limit 2 offset 0)
SELECT * FROM get_page(2,0);

-- удалить Cat
CALL delete_user_by_value('Cat');
*/
