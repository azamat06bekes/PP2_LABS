import re

def match_pattern(w):
    pattern = r"ab*"
    return bool(re.search(pattern, w))

text = input("Enter a string: ")
if(match_pattern(text)):
  print("Matches the pattern:", text)
else:
  print("Does not match the pattern:", text)
