# 10th Task

My_list = list(map(int, input(" Enter a numbers: ").split()))

def func_sort_list(My_list):
    new_list = []
    for num in My_list:
        if (My_list.count(num) == 1):
            new_list.append(num)
    return new_list

print(func_sort_list(My_list))

