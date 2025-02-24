
import random






def gen(min_value, max_value):
    return random.randint(min_value, max_value)
random_number = gen(1, 1000)

guess_history = []
while True:
    x = int(input("Guess a number from 1 to 1000")) 
    guess_history.append(x)
    if x == random_number:
        print("Correct!")
        break
    elif x > random_number:
        print("The number is less than your input, please try again.")
    else:  
        print("The number is greater than your input, please try again.")

print("Here is your history",guess_history)
