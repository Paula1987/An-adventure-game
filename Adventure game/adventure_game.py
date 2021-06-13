import time

import random


def print_pause(text):
    print(text)
    time.sleep(2)


def intro(enemy):
    print_pause("There´s a world unknown for you, "
                "is full of magic, but is counting on you.")
    print_pause("The wind whispers that a " + enemy + " is "
                "planning to attack this world and you're "
                "the only warrior brave enough to face it.")
    print_pause("The path in front of you leads to a ruined cathedral.")
    print_pause("The path on you right leads to a dark cave.")
    print_pause("The path on your left leads to a glowing lake.")
    print_pause("You have your leather armor and your loyal knife.\n")


def play_game(enemy, weapon, protection, items):
    print_pause("Enter 1 to choose the ruined cathedral's path.")
    print_pause("Enter 2 to choose the cave's path.")
    print_pause("Enter 3 to choose the glowing lake's path.")
    print_pause("What would you like to do?")
    choice = input("(Please enter 1, 2 or 3).\n")
    if choice == '1':
        cathedral(enemy)
        fight_run(enemy, weapon, protection, items)
    elif choice == '2':
        cave(enemy, weapon, protection, items)
    elif choice == '3':
        glowing_lake(enemy, weapon, protection, items)
    else:
        play_game(enemy, weapon, protection, items)


def cathedral(enemy):
    print_pause("You enter silently into the ruined cathedral, "
                "when a chill runs down your spine.")
    print_pause("Rapidly, without expecting it, a "
                + enemy + " appears in front of you.")
    print_pause("With an evil laugh the " + enemy + " attacks you!")


def cave(enemy, weapon, protection, items):
    if weapon in items:
        print_pause("The Oracle approaches you and tells you "
                    "to use your " + weapon + " wisely.")
    else:
        print_pause("As you enter the cave the stalactics "
                    "start falling down.")
        print_pause("With agility and artfullness "
                    "you managed to avoid them.")
        print_pause("Finding yourself in front of the Oracle.")
        print_pause("So you've came for the " + weapon + ".")
        print_pause("Give me your knife he says.")
        print_pause("With this ritual your knife become the " + weapon + ".")
        items.append(weapon)
    print_pause("You are back on the crossroads.\n")
    play_game(enemy, weapon, protection, items)


def glowing_lake(enemy, weapon, protection, items):
    print_pause("You walk into the shores when all of a sudden "
                "the lake begins to swirl, emerging mermaids "
                "to the surface.")
    if protection in items:
        print_pause("The mermaids of the glowing lake greet you "
                    "and tell you that you have their gift.")
    else:
        print_pause("The mermaids greet you and bless you with the "
                    + protection + ".")
        print_pause("Now you can defend yourself like "
                    "truthful warrior.")
        items.append(protection)
    print_pause("You are back on the crossroads.\n")
    play_game(enemy, weapon, protection, items)


def fight_run(enemy, weapon, protection, items):
    decision = input("Would you like to (1) fight or (2) run away?\n")
    if decision == '1':
        fight(enemy, weapon, protection, items)
        play_again()
    elif decision == '2':
        crossroads(enemy, weapon, protection, items)
    else:
        fight_run(enemy, weapon, protection, items)


def fight(enemy, weapon, protection, items):
    if weapon in items and protection in items:
        print_pause("The " + enemy + " try to attack, "
                    "but your " + protection + " defends you like no other.")
        print_pause("Then the " + enemy + " sees your " + weapon + " and "
                    "realized the magic power within it.")
        print_pause("The " + enemy + " Knows it's a lost battle "
                    "and runs away never to return!")
        print_pause("Thanks to you, the magic world is free from the "
                    + enemy + "."
                    "You are victorious!")
    elif weapon in items:
        print_pause("You give your best shot with your new "
                    + weapon + ", sadly, you had no protection "
                    "and the " + enemy + " takes your life.")
    elif protection in items:
        print_pause("Your new " + protection + " is great but alone"
                    "is not good enough and you pay the price "
                    "with you life.")
    else:
        print_pause("Although you have a warrior heart, your "
                    "loyal knife and your leather armor are "
                    "not enough to confront the " + enemy + ".")
        print_pause("You have been defeated!")


def crossroads(enemy, weapon, protection, items):
    print_pause("You run away to the crossroads.\n"
                "Fortunately, your intact.")
    play_game(enemy, weapon, protection, items)


def play_again():
    question = input("Would you like to play again?(yes/no)\n").lower()
    if "yes" == question:
        print_pause("Excellent! Restarting the game...")
        adventure_game()
    elif "no" == question:
        print_pause("Thanks for playing! See next time.")
        exit(0)
    else:
        play_again()


def adventure_game():
    items = []
    enemy = random.choice(["Troll", "Dragon", "Witch",
                           "Goblin", "Wickied fairy", "Necromancer"])
    protection = random.choice(["Shield of light", "Armor of warriors",
                                "Flying boots"])
    weapon = random.choice(["Sword of bravery", "Bow of nimbleness",
                            "Spear of destiny"])
    intro(enemy)
    play_game(enemy, weapon, protection, items)


adventure_game()
