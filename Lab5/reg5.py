import re

def match_pattern(text):
  p = r"ab$"
  return bool(re.search(p, text))

text = input("Enter a string: ")
if(match_pattern(text)):
  print("Matches the pattern:", text)
else:
  print("Does not match the pattern:", text)
