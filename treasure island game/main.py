print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("Which way would you like to go, left or right? ").lower()
if choice1 == "left":
    choice2 = input(
        "You get to a river but a storm starts, do you swim or wait? ").lower(
        )
    if choice2 == "wait":
        choice3 = input(
            "You find an old house, which door do you use, red, yellow or blue? "
        )
        if choice3 == "red":
            print("You are attacked by a 700-year-old ghost.\n GAME OVER")
        elif choice3 == "yellow":
            print("You found the treasure.\n CONGRATULATIONS, YOU WIN!")
        else:
            print("You meet the Grim Reaper and you die.\n GAME OVER")

    else:
        print("You are attacked by a crocodile.\n GAME OVER!")
else:
    print(
        "You accidentally enter a spaceship and you are abducted.\nGAME OVER!")
