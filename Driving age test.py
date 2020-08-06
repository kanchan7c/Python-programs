print("Enter your age")
Age = int(input())
if Age < 7 or Age > 100:
    print("Error: Age should be between 7 and 100")
else:
    if Age < 18:
        print("you can't drive")
    elif Age == 18:
        print("Please take driving test")
    else:
        print("you can drive")
