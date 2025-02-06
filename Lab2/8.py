# Python While Loops


# 1st question: Which statement is a correct syntax to break out of a loop?
#Answer: break

# 2nd question: Print i as long as i is less than 6.
i = 1
while i < 6:
    print(i)
    i += 1
#Answer: while, :

# 3rd question: Stop the loop if i is 3
i = 1
while i < 6:
    if i == 3:
        break
    i += 1
#Answer: break

# 4th question: In the loop, when i is 3, jump directly to the next iteration.
i = 1
while i < 6:
    if i == 3:
        continue
    print(i)
#Answer: continue

# 5th question: Print a message once the condition is false.
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
#Answer: else: