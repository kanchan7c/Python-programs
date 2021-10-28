num1 = int (input("Enter First number:"))
num2 = int (input("Enter Second number:"))
operation = input("Enter the operation:")

if operation == "add" :
    if num1 == 56 and num2 == 9 :
        print("Result = 77")
    else:
        print("Result = ", num1 + num2)
elif operation == "subtract" :
    if num1 > num2:
        print("Result = ", num1 - num2)
    else:
        print("Number 1 should be greater than number 2")
elif operation == "multiply" :
    if num1 == 45 and num2 == 3 :
        print("Result = 555")
    else:
        print("Result = ", num1 * num2)
elif operation == "divide" :
    if num1 == 56 and num2 == 6 :
        print("Result = 4")
    elif num2 == 0:
        print("Number 2 can't be zero")
    else:
        print("Result = ", num1 / num2)
else:
    print("Wrong operator, please enter add, subtract, multiply or divide")
