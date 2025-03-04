def func(my_tuple):
    new_list = []
    for i in my_tuple:
        if i.isdigit():  
            new_list.append(int(i))
        else:
            new_list.append(i)

    return tuple(new_list) 

my_tuple = tuple(input("Enter elements separated by commas: ").split(","))

result = all(func(my_tuple))
print(result)
