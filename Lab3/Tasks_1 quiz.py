# 1st Task:

name = input("Enter your name: ")
age = input("Enter your age: ")
if(int(age)):
    if(age >= 18):
        print("Name: ", name, "Age: ", age, "Status: ", "You are an adult")
    else:
        print("Name: ", name, "Age: ", age, "Status: ", "You are a minor")
else:
    age = int(age)
    if(age >= 18):
        print("Name: ", name, "Age: ", age, "Status: ", "You are an adult")
    else:
        print("Name: ", name, "Age: ", age, "Status: ", "You are a minor")

