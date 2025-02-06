# 13th Task

import random

cnt_guesses = 0
print("Hello! What is your name?")
name = input("")
print("Well,", name, "I am thinking of a number between 1 and 20.")
random_num = random.randint(1, 20)
button = 'n'
button_1 = 's'
while(button != button_1):
    print("Take a guess.")
    num = int(input())
    if(num > random_num):
        print("Your guess is too high.")
        cnt_guesses += 1
        
    elif(num < random_num):
        print("Your guess is too low.")
        cnt_guesses += 1
        
    elif(num == random_num):
        print("Good job, ", name, "! ", "You guessed my number in ", cnt_guesses, " guesses!")
        
    elif(cnt_guesses > 0):
        button = 'n'
