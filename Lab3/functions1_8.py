# 8th Task

def has_007(numbers):
    for i in range(len(numbers)-1):
        found_0 = False
        found_00 = False
        for num in numbers:
            if(num == 0 and not found_0):
                found_0 = True
            elif(num == 0 and found_0 and not found_00):
                found_00 = True
            elif(num == 7 and found_00):
                return True
    return False

numbers = [7, 0, 3, 0, 3, 2, 8, 7]
print(has_007(numbers))

