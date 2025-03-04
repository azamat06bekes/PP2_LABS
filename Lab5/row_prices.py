import re

path = "C:\\Users\\админ\\OneDrive - АО Казахстанско-Британский Технический Университет\\Рабочий стол\\PP2_practice\\row.txt"

with open(path, 'r', encoding='utf-8') as file:
    text = file.read()

pattern = r"\d{1,3}(?: \d{3})*,\d{2}"
prices = re.findall(pattern, text)
    
print(prices)