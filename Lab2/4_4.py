# Python - Unpack Tuples


# 1st question: Consider the following code:
fruits = ('apple', 'banana', 'cherry')
(x, y, z) = fruits
print(y)
# What will be the value of y?
#Answer: banana

# 2nd question: Consider the following code:
fruits = ('apple', 'banana', 'cherry')
(x, *y) = fruits
print(y)
# What will be the value of y?
#Answer: ['banana', 'cherry']

# 3rd question: Consider the following code:
fruits = ('apple', 'banana', 'cherry', 'mango')
(x, *y, z) = fruits
print(y)
# What will be the value of y?
#Answer: ['banana', 'cherry']
