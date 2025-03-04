import string

for letter in string.ascii_uppercase:
  filename = f"{letter}.txt"
  with open(filename, 'w', encoding='utf-8') as file:
    file.write(f"This is {filename}")

