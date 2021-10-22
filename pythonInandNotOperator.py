#:::::::::::::::::::::::::::::::::::::::::::
# IN operator

my_num = input("Enter the number  ")
options = [2, 4, 9, 78, 62, 3, 7]

if int(my_num) in options:
    print(f"{my_num} is a valid option")
else:
    print("wrong choice, try again!") 

#:::::::::::::::::::::::::::::::::::::::::::
# NOT operator

trip = True

if not trip:
    print("No trip")

name = "Cookie"

if name not in ['trip', 'eating']:
    print(f"{name} is not a part of trip")

#:::::::::::::::::::::::::::::::::::::::::::
