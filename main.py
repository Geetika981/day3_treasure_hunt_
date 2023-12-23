print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Welcome to treasure Island.")
print("Your mission is to find the trasure.")
a = input("You're at a cross road.Where do you want to go? Type 'left' or 'right'\n").lower()
if a == "left":
    b=input("You've come to a lake.There is an island in the middle of a lake. Type 'wait' to wait for a boat. Type 'swim' to swim across\n").lower()
    if b == "wait":
        c = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n").lower()
        if c == "yellow":
            print("You found the treasure. You Win!!")
        elif c == "red":
            print("It's a room full of fire. Game Over!!")
        elif c == "blue":
            print("You enter a room full of beasts. Game Over!!")
        else:
            print("You have entered a room that doesn't exist. Game Over!!")
    else:
        print("You got attacked by angry trout. Game Over!!")

else:
    print("You fell into a hole")
    print("Game Over!!:-(")
