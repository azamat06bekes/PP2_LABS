import re

def to_split(text):
  return re.findall(r'[A-Z][a-z]*', text)

text = input("Enter a string: ")
print(to_split(text))
