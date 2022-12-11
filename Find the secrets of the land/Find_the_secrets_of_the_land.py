import os
import time
import random

# Initialise variables
playerName = ""
playerSpecies = ""
playerHealth = 1
strength = 1
money = 100
gun = True
ammo = 0
bear = True

def RollDice(side): # Used for dice roll segments
    result = random.randint(1,side)
    return result

def EnterContinue(): # Press enter to continue the program
    input("Press enter to continue... ")
    print("")

def CreateCharacter(): # Create the player character
    global name
    global species
    global health
    global strength
    name = input("What is your name? ")
    species = input("What is your species? ")
    health = ((RollDice(6) * RollDice(12)) +10)
    strength = ((RollDice(6) * RollDice(14)) +8)
    print(" ")
    print(f"HEALTH: {health}")
    time.sleep(1)
    print(f"STRENGTH: {strength}")
    time.sleep(1)
    print("")

def StartVillage(): # The first part of the game
    global bear
    global ammo
    print("There are three roads, each heading in different directions.")
    choice = input("Do you head 'North', 'East', or 'West'? ").lower()
    if choice == "west": # Go west of the start position
        print("")
        print("You head west. A few markets can be found along with an exit gate.")
        time.sleep(1)
        if bear:
            print("However, there is a bear standing in the way. It looks strong and dangerous. It could kill you easily.")
            time.sleep(1)
            if ammo != 0:
                while shootBear != yes or shootBear != no:
                    shootBear = input("Will you shoot the bear? 'Yes' or 'No'").lower
                    if shootBear == "yes":
                        ammo -= 1
                        bear = False
                        print("You shoot the bear. It dies instantly. All the onlookers congratulate you and you can now carry on forwards")

                    elif shootBear == "no":
                        print("You decide not to shoot the bear and head backwards.")
                        StartVillage()
                    else:
                        print("I didn't understand that.")
            else:
                print("While you have a gun to shoot the bear, you don't have any ammo for it. Therefore, you head backwards.")
                time.sleep(1)
                print("")
                StartVillage()
        else:
            westOfStart()

    elif choice == "east":
        print("You head east. ")

    elif choice == "north":
        print("You head north. ")

    else:
        print("I didn't understand that.")
        StartVillage()

def westOfStart():
    choice = input("Where do you want to go? The 'bar', the 'Weapon Store', the 'restaurant', or the house belonging to the 'Mayor'? ").lower()
    if choice == "bar":

    elif choice == "restaurant":

    elif choice == "mayor":

    elif choice == "weapon store":

    else:
        print("""I didn't understand that.
""")
        westOfStart()

# Starting text
def begin():
    print("""It's been a few days since you broke out of that crazed old man's cell. You really enjoyed the moment you finally got to see green grass and a blue sky.
    
You come across a small village where you decide to take refuge before deciding where to head to next.
""")
    EnterContinue()
    print("""Suddenly, you start to think. You think about how you even ended up in that cell.
You wonder who had you thrown in there, and you try to conceive on whether this was all part of a plan.
""")
    EnterContinue()
    print("You decide that you will find the answers yourself, no matter what it takes.")
    EnterContinue()
    CreateCharacter()
    print(f"This is the beginning of {name} the {species}'s journey. It will be a great one indeed.")
    EnterContinue()
    print("You enter the village through the open gate and come across a cross junction.")
    StartVillage()

begin()