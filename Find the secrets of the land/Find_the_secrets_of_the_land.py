import time
import random

# Initialise variables
name = ""
species = ""
health = 1
strength = 1
money = 100
ammo = 0
bear = True
talkedToDrunkard = False

# Initialise inventory
inventory = ["Gun"]

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

# Using inventory items
def HealthKitUse():
    global inventory
    global health
    if "HealthKit" in inventory:
        print("You used a health kit.\nYou gain 30 health.")
        health += 30
    else:
        print("You don't have a health kit.")

def Bar(): # Enter the bar
    global money
    global health
    global talkedToDrunkard
    print("""
You enter the bar. A bartender greets you and offers you a pint of beer.
The beer costs 10 Money.""")
    if money >= 10:
        buybeer = input("Will you buy this beer? 'Yes' or 'no'?").lower()
        if buybeer == "yes" or buybeer == "n":
            money -= 10
            health += 5
            print("")
            print("That beer tasted nice. You gain 5 health.")
        elif buybeer == "no" or buybeer == "n":
            print("")
            print("You decide not to buy this beer.")
        else:
            print("""I didn't understand that
            """)
            bar()
    else:
        print("Unfortunately you don't have enough money.")
    print()
    print("The bar is largely empty, except for a drunkard sitting at one of the tables.\n")
    time.sleep(1)
    if not talkedToDrunkard:
        choice = input("Do you want to talk to him? 'Yes' or 'No'?").lower()
        if input == "yes":
            print("""
    You walk up to the drunkard. You sit down next to him and he starts a conversation.\n""")
            print("""'You look like you've come from very far away. In any case, nothing like a good beer to get yourself refreshed.
    I heard that there is some demonic king out there who is locking people who he deems 'inadequate'.'""")
            EnterContinue()
            print("'Wait, from what you told me, it seems like you were victim to his scheme. That must suck.'")
            EnterContinue()
            print("'Look. I'm just a mere drunkard so I can't help much, but take some ammo for your gun. And this health kit. I hope this will be useful to you.'")
            ammo += 16
            inventory.append("HealthKit")
            print("You acquire a health kit.")
            time.sleep(1)
            print("You decide to leave the bar.\n")
            time.sleep(2)
        else:
            print()
            print("You decide not to talk to the drunkard and leave the bar.")
            WestOfStart()
    else:
        print("But you don't want to disturb him again, so you leave the bar.\n")
        time.sleep(1)
        WestOfStart()

def WestOfStart(): # You head west and the bear is dead
    choice = input("Where do you want to go? The 'bar', the 'Weapon Store', the 'restaurant', or the house belonging to the 'Mayor'? ").lower()
    if choice == "bar":
        bar()

    elif choice == "restaurant":
        restaurant()

    elif choice == "mayor":
        mayor()

    elif choice == "weapon store":
        weaponstore()

    else:
        print("""I didn't understand that.
""")
        westOfStart()

def StartVillage(): # The first part of the game
    global bear
    global ammo
    global inventory
    shootBear = ""
    print("There are three roads, each heading in different directions.")
    choice = input("Do you head 'North', 'East', or 'West'? ").lower()
    if choice == "west": # Go west of the start position
        print("")
        print("You head west. A few markets can be found along with an exit gate.")
        time.sleep(1)
        if bear: #The bear is not dead
            print("However, there is a bear standing in the way. It looks strong and dangerous. It could kill you easily.")
            time.sleep(1)
            if ammo != 0 and "Gun" in inventory:
                while shootBear != "yes" or shootBear != "no":
                    shootBear = input("Will you shoot the bear? 'Yes' or 'No'").lower()
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
        else: # The bear is dead
            westOfStart()

    elif choice == "east":
        print("You head east. ")

    elif choice == "north":
        print("You head north. ")

    else:
        print("I didn't understand that.")
        StartVillage()

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