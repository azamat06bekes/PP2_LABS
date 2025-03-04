import re

def snake_to_camel(new_text):
  
  return re.sub(r'_([a-zA-Z])', lambda match: match.group(1).upper(), new_text)

text = input("Enter a string: ")
new_text = re.sub(r"[ .,]", "_", text)
print(snake_to_camel(new_text))
