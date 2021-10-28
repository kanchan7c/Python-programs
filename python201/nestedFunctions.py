def name1(name):  
    print("Welcome ", name)

    def name2():
        print("Welcome ", name)
    name2()                 #also known as Decorator

name1("Samaira")

#nested functions don't need the variable value inside each function. When they don't find the value in nested functions, it looks over to it's parent function for the value of variable. 