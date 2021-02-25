#
#
#

#imports
import random



#functions

def dice():
    multi_dice = input("Would you like to tempt fate? (Yes/No): ")

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
        more_rolling = input("Roll more dice? (Yes/No): ")
        if more_rolling == "No":
            stop()
            break
                
        
def go_again():

    while True:
        answer = input("Roll more dice? (Yes/No): ")
        if answer == "Yes":
            main() #< --- recursive function
        if answer == "No":
            stop()
            break

        
def stop():
    while True:
        answer = input("Exit? (Yes/No): ")
        if answer == "No":
            main()
        if answer == "Yes":
            print("Good luck, have fun!")
            exit()
            break
        


#main function
def main():
    dice()
    go_again()
    stop()





main()
