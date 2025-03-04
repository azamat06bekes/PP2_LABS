import re

def camel_to_snake(text):
  return re.sub(r'(?<!^)(?=[A-Z])', '_', text)

text = input("Enter a string: ")
print(camel_to_snake(text))

