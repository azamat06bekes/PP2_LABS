# 6th Task


numbers = list(map(int, input("Enter numbers: ").split()))

prime_numbers = list(filter(lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1)), numbers))

print("Prime numbers: ", prime_numbers)