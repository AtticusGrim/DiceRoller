#
#
# Dice

import random

dice = input("Enter your dice: ")

d20 = random.randint(1, 20)
d10 = random.randint(1, 10)
d6 = random.randint(1, 6)
d4 = random.randint(1, 4)

if dice == "d20":
    print("Result: ", d20)
    
elif dice == "d10":
    print("Result: ", d10)

elif dice == "d6":
    print("Result: ", d6)
          
elif dice == "d4":
    print("Result: ", d4)

roll_again = input("Would you like to roll again? ")

while True:
    if roll_again == "yes":
        dice = input("Enter your dice: ")
        if dice == "d20":
            print("Result: ", random.randint(1,20))
        elif dice == "d10":
            print("Result: ", random.randint(1,10))
        elif dice == "d6":
            print("Result: ", random.randint(1, 6))
        elif dice == "d4":
            print("Result: ", random.randint(1, 4))

        roll_again = input("Would you like to roll again? ")


    if roll_again == "no":
        print("Good luck, have fun!")
        break
    
    
