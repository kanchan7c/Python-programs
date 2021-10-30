import math


class bank:

    def withdraw():
        try:
            withdrawAmount = int(
                input("How much would you like to withdraw? \n"))
            if(withdrawAmount != 0 or math.isnan(withdrawAmount)):
                with open('balanceSheet.txt', 'a') as file:
                    file.write(f"Withdrawl made of Rupees {withdrawAmount}\n")
                    print(f"{withdrawAmount} is withdrawn")
            else:
                print("No withdrawls made\n")
        except Exception:
            print("Invalid input")

    def deposit():
        try:
            depositAmount = int(
                input("How much would you like to deposit? \n"))
            if(depositAmount != 0 or math.isnan(depositAmount)):
                with open('balanceSheet.txt', 'a') as file:
                    file.write(f"Deposit made of Rupees {depositAmount}\n")
                    print(f"{depositAmount} is withdrawn")
            else:
                print("No deposit made\n")
        except Exception:
            print("Invalid input")

    while True:
        request1 = input("Do you want to withdraw? y/n \n")
        request1 = request1.lower()

        if(request1 == 'y' or request1 == 'n'):
            if(request1 == 'y'):
                withdraw()
            else:
                request2 = input("Do you want to deposit? y/n \n")
                request2 = request2.lower()
                if(request2 == 'y' or request2 == 'n'):
                    if(request2 == 'y'):
                        deposit()
                    elif (request1 == 'n' and request2 == 'n'):
                        print("Thank you for banking with us.\n")
                        break
        else:
            print("Incorrect input, try again")


transactions = bank()
print(transactions)
