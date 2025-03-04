import re

def match_pattern(text):
    p = r"ab{2,3}"
    return bool(re.fullmatch(p, text))

text = input("Enter a string:")
if(match_pattern(text)):
    print("Matches the pattern: ", text)
else:
    print("Does not match the pattern: ", text)
