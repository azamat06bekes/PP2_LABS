import re

path = "C:\\Users\\админ\\OneDrive - АО Казахстанско-Британский Технический Университет\\Рабочий стол\\PP2_practice\\row.txt"

with open(path, 'r', encoding='utf-8') as file:
    text = file.read()

pattern = r"\d{3}-\d{3}"

num_of_CR = re.findall(pattern, text)
print(num_of_CR)
