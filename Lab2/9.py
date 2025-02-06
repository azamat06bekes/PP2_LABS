# Python For Loops


# 1st question: What will be the result of the following code:
for x in range(3):
    print(x)
#Answer: 0 1 2

# 2nd question: Loop through the items in the fruits list.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
#Answer: for, in, :

# 3rd question: In the loop, when the item value is "banana", jump directly to the next item.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
#Answer: continue

# 4th question: Use the range function to loop through a code set 6 times.
for x in range(6):
    print(x)
#Answer: range(6)

# 5th question: Exit the loop when x is "banana".
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
#Answer: break