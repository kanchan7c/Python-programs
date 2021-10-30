# Writing class in python

# Example 1
class addNumbers:
    num1 = int(input("Enter 1st number : \n"))
    num2 = int(input("Enter 2nd number : \n"))
    result = num1 + num2

add = addNumbers()
print(f"Result = {add.result}")


## Example 2
class dog:
    dog1 = {
        "name" : "Cookie",
        "color" : "Brown",
        "type" : "Agressive"
    }

myDog = dog()

print(f"My dog is {myDog.dog1['name']}, she is of {myDog.dog1['color']} color and she is very {myDog.dog1['type']}")

# Decorators 

def abc(func):
    def wrapper():
        print("1st print")
        func()
        print("2nd print")
    return wrapper

@abc    # this is a decorator
def fun2():
    print("fun2")
