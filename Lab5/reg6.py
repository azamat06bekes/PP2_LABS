import re

def match_pattern(text):
  return re.sub(r"[ .,]", ":", text)

text = input("Enter a string: ")
print(match_pattern(text))