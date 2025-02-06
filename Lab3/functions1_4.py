# 4th Task

numbers = list(map(int, input("Enter a number with space: ").split()))

prime_numbers = []
def filter_prime(numbers):
    for num in numbers:
        cnt_num = 0
        if(num < 2):
            continue
        else:
            for i in range(2, num):
                if(num % i == 0):
                    cnt_num += 1
            if(cnt_num == 0):
                prime_numbers.append(num)        

    return prime_numbers

prime_nums = filter_prime(numbers)
print("Prime numbers: ", prime_nums)
