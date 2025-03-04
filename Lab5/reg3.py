import re

def match_pattern(text):
  pat = r"[a-z]+_[a-z]+"
  return bool(re.fullmatch(pat, text))

text = input("Enter a string: ")
if(match_pattern(text)):
  print("Matches the pattern:", text)
else:
  print("Does not match the pattern:", text)
