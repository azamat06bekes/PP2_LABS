import re

def to_insert(text):
  return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

text = input("Enter a string: ")
print(to_insert(text))
