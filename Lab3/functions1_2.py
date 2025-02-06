# 2nd Task

def func_2(fahrenheit):
    celsius = (5/9) * (fahrenheit - 32)
    return celsius
far_value = float(input("Enter number of fahrenheit: "))
celsius_v = func_2(far_value)
print(f"{far_value} Fahrenheit = {celsius_v:.2f} Celsius")
