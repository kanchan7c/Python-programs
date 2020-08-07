a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))

def add():
    print("result:", a+b)

def sub():
    print("result:", a - b)

def multiply():
    print("result:", a*b)

def divide():
    print("result:", a/b)

def choose():
    c=input("Select an Operator of your choice:\n + for Add\n - for Subract\n x for Multiply\n \\for divide\n")
    if c == "+":
        add()
    elif c == "-":
        sub()
    elif c == "x":
        multiply()
    elif c == "\\":
        divide()

choose()
