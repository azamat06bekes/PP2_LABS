# Python If ... Else


# 1st question: What will be the result of the following code:
x = 5
y = 8
if x > y:
  print('Hello')
else:
  print('Welcome')
#Answer: Welcome

# 2nd question: Print "Hello World" if a is greater than b.
a = 50
b = 10
if a > b:
    print("Hello World")
#Answer: if, >, :

# 3rd question: Print "Hello World" if a is not equal to b.
a = 50
b = 10
if a != b:
    print("Hello World")
#Answer: if, !=, :

# 4th question: Print "Yes" if a is equal to b, otherwise print "No".
a = 50
b = 10
if a == b:
    print("Yes")
else: 
    print("No")
#Answer: if, ==, :, else:

# 5th question: Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
a = 50
b = 10
if a == b:
    print("1")
elif a > b:
    print("2")
else: 
    print("3")
#Answer: if, ==, :, elif, >, else:

# 6th question: Print "Hello" if a is equal to b, and c is equal to d.
if a == b and c == d:
  print("Hello")
#Answer: and

# 7th question: Print "Hello" if a is equal to b, or if c is equal to d.
if a == b or c == d:
  print("Hello")
#Answer: or

# 8th question: Complete the code block, print "YES" if 5 is larger than 2.
# Hint: remember the indentation.
if 5 > 2:
    print("YES")
#Answer: print("YES")

# 9th question: Use the correct one line short hand syntax to print "YES" if a is equal to b, otherwise print("NO").
a = 2
b = 5
print("YES") if a == b else print("NO")
#Answer: print("YES") if a == b else print("NO")
