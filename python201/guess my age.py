age = 67
Choices = 5
print("**Guess my age game**\nYou have 5 choices. All the best!!!")
while (Choices>0) :
    number = int(input("\nGuess my age"))
    if number > age and Choices >= 1 :
        print("I'm younger :)")
        print("You have ", Choices - 1, " choices left")
        Choices = Choices - 1
        continue
    elif number < age  and Choices >= 1 :
        print("I'm older :(")
        print("You have ", Choices - 1, " choices left")
        Choices = Choices - 1
        continue
    elif number == age:
        print("Congratulations! You have guessed my age.")
        break
print("GAME OVER!!!")
