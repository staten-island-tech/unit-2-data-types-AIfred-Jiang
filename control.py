""" def login(password):
    #if statement evaluates to true
    if password == "secret":
        print("login")
    else:
        print("incorrect")
login("secret")
 """
def grade(score):
    if score >=92:
        print("A")
    elif score >=82:
        print("B")
    elif score >=72:
        print("C")
    else:
        print("F")
grade(105)