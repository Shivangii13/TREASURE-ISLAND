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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("WELCOME TO TREASURE ISLAND")
print("your mission is to find the treasure.")
choice1 = input('You are at a crossroad, where do you want to go? Type "left" or "right".').lower()

if choice1 == "left":
 choice2 =input('you have come to a lake, There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across').lower()
 if choice2 == "wait":
    choice3 = input("you arrive at the island unhharmed. There is a house with 3 doors. one red, one yellow and one blue. Whivh colour do you want to choose?")
    if choice3 == "red":
      print("its a room full of fire. GAME OVER.")
    elif choice3 == "yellow":
      print("you found treasure. YOU WIN!")
    elif choice3 == "blue":
      print("you enter a room of beasts. GAME OVER")
    else:
      print("you choose the door that does not exist. GAME OVER")
    
 else:
   print("you got attend by angry trout. GAME OVER")

else:
   print("you fell into a hole, GAME OVER. ")



