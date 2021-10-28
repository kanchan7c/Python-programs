print("Hello World")
#::::::::::::::::::::::::::::::::::::::::::::
# Data types 
name = "Kanchan" #String
number = 99 #Integers
number2 = 3.14 #float
lisT = ["item1", "item2", 32, 92.3] #list which is typically an Array
tuplE = ("item1", 32, 92.3) #tuples are immutable
sets = {"item1", "item2", 292} #sets don't maintain the order of items
dictionary = {
    "key" : "value",
    "key2" : "value2",
}
boolean = True # or False
none = None 
print(name.upper())

#::::::::::::::::::::::::::::::::::::::::::::
lst = ['Name', 27, ['baby', 'cookie'], 'food'] # list can be variables too
lst.append("garden")
lst.remove("food")
for item in lst:
    print(item)
lst.reverse()
for item in lst:
    print(item)

#::::::::::::::::::::::::::::::::::::::::::::
person = {                    #Example of a dictionary
    "name" : "kanchan",
    "age" : 27,
    "pet" : "Cookie",
    "food" : {
        "fav" : "icecream",
        "badFood" : "mushroom"
    }
}
print(person["age"])
del person["pet"] #delete the mentioned value

#::::::::::::::::::::::::::::::::::::::::::::
animals = ('dog', 'cat', 'lion',) #tuple: it can't be changed. Nothing can be added to a tuple, not too many functions can be done on tuple. It can used for unchangeable list 
for animal in animals:
    print("The animal is", animal)

setOfValues = {"firstName", "lastName", "age", "pet"} #set and won't maintain order. Only unique items can be added. It omits the duplicate values
print(setOfValues)

#::::::::::::::::::::::::::::::::::::::::::::
python = True  #boolean example
Java = False 
if True == True:
    print("It is correct")

#::::::::::::::::::::::::::::::::::::::::::::
money = None #empty variable without data type which is to be rewritten later

#::::::::::::::::::::::::::::::::::::::::::::
list2 = ["one", 2, 892.2, ["two"], "three",] #example of indexing & slicing
print(list2[3])
print(list2[0:2]) # Start at index 0 to 2 and print the values
print(list2[2::]) # Start at index 2 to the end and print the values
print(list2[-2::]) #start reverse and grab from -2 till the end

#::::::::::::::::::::::::::::::::::::::::::::
input() #getting input from use. The input comes as String
age = input('What is your age')
age = int(age) #casting into integer
type(age) #checking the data type of age

#::::::::::::::::::::::::::::::::::::::::::::
name = "Kanchan"  #print formatting using format function
greeting = "Hello {}, welcome to Python".format(name)
print(greeting)
name = "Cookie"    #print formating using f string
message = f"{name} is a brown dog"
print(message)

#::::::::::::::::::::::::::::::::::::::::::::
if True == True:  #comparison operator which compares only values. nesting can be done by using elif
    print(True)

age = int(input('What is your age'))
if age >= 18:
    print('You can vote')
    greeting = "Hi!"
else:
    print('You are not eligible to vote')
    greeting = "Hi!"
print(f"{greeting} Welcome here.")

# > 
# >=
# <=
# ==
# !=

#::::::::::::::::::::::::::::::::::::::::::::

age = 27
name = "Kanchan"
if age >= 18 and name == "Kanchan": #both needs to be true
    print("I am true")
else:
    print("I am false")

age = 27
name = "Cookie"
if age >= 18 or name == "Kanchan": #one of the condition needs to be true
    print("I am true")
else:
    print("I am false")

#::::::::::::::::::::::::::::::::::::::::::::
#Loops
travel_bag = ["clothes", "Bottle", "Milk", "Food", "Money"]
for items in travel_bag:
    if items == "Bottle" or items == "Milk":
        name = input('Enter your name')
        print(f"Hello {name}, {items} is a  baby item")

person = {
    "Name:" : "Kanchan",
    "Age:" : 27,
    "Pet:" : "Cookie"
}
for key, value in person.items():
    print(key, value)

num = 0
while num <= 100:
    print(num)
    num = num + 10

#continue keyword skips the condition value and print everything else
#break keyword breaks the loop when condition matches before break statement
num = 0
while num <=100 :
    num = num + 1
    if num * 2 == 10:
        break
    else:
        print(num)

#::::::::::::::::::::::::::::::::::::::::::::
#functions

def functionName(name):  #syntax to define function in python. Function can take multiple parameters
    print(f"Hello, {name}")
functionName(input("Enter your name"))

def add(num1, num2):
    total = num1 + num2
    return print(total)   
num1 = int(input("Enter num1  "))
num2 = int(input("Enter num2  "))
add(num1, num2)

#::::::::::::::::::::::::::::::::::::::::::::

#python3 -m http.server -- to find the localhost server address

#::::::::::::::::::::::::::::::::::::::::::::

import random
user_choice = input("Choose one from: Rock , Paper, and Scissor :  ")


if random.choice(["Rock", "Paper", "Scissor"])== user_choice :
    print("You won")
else:
    print("You lose")

#::::::::::::::::::::::::::::::::::::::::::::

#Rock paper Scissor game

import random
name = input("Enter player name:  ")

while True:
    user_choice = input("Choose one from: Rock , Paper, and Scissor :  ")
    if random.choice(["Rock", "Paper", "Scissor"]) == user_choice.capitalize() :
        print(f"{name}, You won!")
        break
    else:
        print("Try again")
        continue

#::::::::::::::::::::::::::::::::::::::::::::