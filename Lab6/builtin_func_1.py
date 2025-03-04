from functools import reduce 

def multiply_num(my_list):
    res = reduce(lambda a, b: a * b, my_list)
    return res

my_list = list(map(int, input("Enter numbers: ").split()))
print(multiply_num(my_list))