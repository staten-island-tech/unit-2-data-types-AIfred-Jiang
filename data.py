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

def word_count(x):
    words = x.split() #splits the sentence into a list of words
    return len(words) #returns the number of words

user_input = input("Please enter a sentence: ") #asking user to type something
word_count(user_input) #
print(f"The number of words in your sentence is: {word_count}")
 