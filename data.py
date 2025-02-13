""" x = 31
y = float(3.356475641)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15] """
""" print(values)
for i in values:
    print(i) """

""" print(values[0])
print(values[6])

x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """
""" 
def word_count(x):
    words = x.split() #splits the sentence into a list of words
    return len(words) #returns the number of words

user_input = input("Please enter a sentence: ") #asking user to type something
word_count(user_input) #
print(f"The number of words in your sentence is: {word_count}")
  """
""" 
day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """
""" 
x = "test"
print(f"hello {x}")

temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" def check_odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print(check_odd_or_even(5646543425)) """
""" 
def service(x):
    if x == "bad":
        print("0 percent tip")
    elif x == "okay":
        print("15 percent tip")
    elif x == "good":
        print("20 percent tip")
    elif x == "great":
        print("25 percent tip")
    else:
        print("Invalid input, please enter 'bad', 'okay', 'good', or 'great'")
""" """ print(service("great")) """

def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

number = int(input("Enter a number: "))
print("Factors of", number, "are:", find_factors(number))

""" def gcf(x,y):
    greatest = []
    for i in range(min(x,y) , 0 , -1):
        if x % i == 0 and y % i == 0:
            greatest.append(i)
    return greatest[0]
print(gcf(222,444))
 """