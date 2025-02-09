# 3rd Task:

n = int(input("Enter a number: "))
def iter(n):
    new_l = []
    for i in range(1, n+1):
        if((i % 3 == 0) and (i % 4 == 0)):
            new_l.append(i)
    return new_l
print(iter(n))

