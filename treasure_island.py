print("Welcome to the treasure island game! \n")
print("Welcome to the treasure island game! \n")

choice1 = input('You\'re see at a crossroad, where do you want to go? Type "left" or "right". ').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in a middle of the lake. Type "wait" to wait for a boat or "swim" to swin across. ').lower()
    if choice2 == "wait":
        choice3 = input('You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ').lower()
        if choice3 == "red":
            print("It's a room full of fire. Game over! ")
        elif choice3 == "yellow":
            print("You found the trasure! You win! ")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game over! ")
        else:
            print("You chose a door that doesn't exist. Game over! ")
    else:
        print("You got attacked by an angry trout. Game Over! ")
else:
    print("You fell into a hole. Game over! ")