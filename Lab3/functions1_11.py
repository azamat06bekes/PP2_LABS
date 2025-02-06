# 11th Task

w = input("Enter a string: ")
s = False
new_w = w.lower()
def is_Palindrome(new_w):
    return new_w == new_w[::-1]

if(is_Palindrome(new_w)):
    print("It is palindrome")
else:
    print("It isn't palindrome")

    