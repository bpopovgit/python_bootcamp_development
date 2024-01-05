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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
choice_one = input("You're at a crossroad, where do you want to go? Type 'left or 'right'. ").lower()
choice_two = ""
choice_three = ""
allowed_doors = ["Blue", "Yellow", "Red"]
doors_lowered = [x.lower() for x in allowed_doors]

if choice_one != "left":
    print("You fell into a hole.\nGame over.")
    exit()

else:
    choice_two = input('You\'ve come to a lake.'
                       ' There is an island in the middle of the lake.'
                       ' Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()

if choice_two != "wait":
    print("You got attacked by an angry trout.\nGame Over.")
    exit()

else:
    choice_three = input('You arrive at an island unharmed. There is a house with 3 doors.'
                         ' One red, one yellow and one blue. Which colour do you choose? ').lower()

if choice_three not in doors_lowered:
    print("Game Over.")
    exit()

elif choice_three == "blue":
    print("You were eaten by Beasts.\nGame Over.")
    exit()

elif choice_three == "red":
    print("You got burned by fire.\nGame Over.")
    exit()

elif choice_three == "yellow":
    print("You found the treasure! You win!")

