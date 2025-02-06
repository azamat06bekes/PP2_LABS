# 7th Task

def has_33(numbers):
    for i in range(len(numbers)-1):
        if(numbers[i] == 3 and numbers[i+1] == 3):
            return True
    return False

numbers = [7, 1, 3, 3, 3, 2, 8, 0]
print(has_33(numbers))

