""" def login(password):
    #if statement evaluates to true
    if password == "secret":
        print("login")
    else:
        print("incorrect")
login("secret")
 """
""" def grade(score):
    if score >=92:
        print("A")
    elif score >=82:
        print("B")
    elif score >=72:
        print("C")
    else:
        print("F")
x = int(input("what the score"))
grade(x) """

""" def gamble(age, id):
    if age >= 21:
        if id:
            print("Gamble Away")
        else:
            print("you're too young")
 """

def gamble(age, id):
    if age >= 21 and id == True:
        print("have fun")
    elif age >= 21 and id == False:
        print(" you need an id verification")
    else:
        print("you're too young")
if not raining == true:
    print("go for walk")
if raining == false:
    print("go for walk")