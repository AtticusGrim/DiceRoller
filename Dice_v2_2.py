#
#
#

import random


multi_dice = input("Would you like to tempt fate? (Yes/No) ")

while True:
    if multi_dice == "Yes":
        num_sides = input("How many sides? ")
        num_dice = input("How many dice? ")
        num_sides = int(num_sides)
        num_dice = int(num_dice)
        for _ in range(num_dice):
            print (random.randint(1, num_sides))
    if multi_dice == "No":
        print("Good luck, have fun!")
        break
    more_rolling = input("Roll more dice? ")
    if more_rolling == "No":
        print("Good luck, have fun!")
        break

print("May the rolls be ever in your favor!")
