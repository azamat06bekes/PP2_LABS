text = input("Enter a string: ")
lower_text = text.lower()
if(lower_text == lower_text[::-1]):
  print("This string is palindrome!")
else: print("This string is not palindrome!")
