import random
from time import sleep

choices = ["Charmander", "Squirtle", "Bulbasur"]

computer = random.choice(choices)

player = False
while player == False:
    name = input("Helo please enter your name: ")
    print(f"Hello, {name} Welcome to pokemon Battle Game!!")
    player = input("Which pokemon do you want to choose?\n'Charmander':'Charmander'\n'Squirtle':'Squirtle'\n'Bulbasur':'Bulbasur'\n'Stop the game':'Stop':")
    if player == computer:
        print("Tie!!")
    elif player == "Charmander":
        if computer == "Squirtle":
            print("\nPlease,Wait we are loading your result...!!")
            sleep(2)
            print("You Lost!!")
        else:
            print("\nPlease,Wait we are loading your result...!!")
            sleep(2)
            print("You Win!!")

    elif player == "Squirtle":
        if computer == "Bulbasur":
            print("\nPlease,Wait we are loading your result...!!")
            sleep(2)
            print("You Lost!!")
        else:
            print("\nPlease,Wait we are loading your result...!!")
            sleep(2)
            print("You Win!!")
    elif player == "Bulbasur":
        if computer == "Charmander":
            print("\nPlease,Wait we are loading your result...!!")
            sleep(2)
            print("You Lost!!")
        else:
            print("\nPlease,Wait we are loading your result...!!")
            sleep(2)
            print("You Win!!")
    elif player == "Stop":
        print("Thanks for playing!!")
        break
    else:
        print("That's not a valid play!")


    player = False
