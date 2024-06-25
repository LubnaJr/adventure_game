import time
import random

def print_sleep(message, wait):
    print(message)
    time.sleep(wait)

def choose_character():
    global character
    print_sleep("You are about to discover a fiary word with all sorts of monsters and creatures!",2)
    print_sleep("choose you character: ",1)  
    print_sleep("1. Ice Wizard: Auron Frostbane\nCommand the relentless power of ice and snow with Auron Frostbane, the wizard whose chilling magic can freeze foes in their tracks and turn the tide of any battle.",3)
    print_sleep("2. Fire Fay: Lyra Emberwing\nUnleash the blazing fury of Lyra Emberwing, the fire fay whose incandescent flames and searing speed ignite the battlefield and inspire awe in allies.",3)
    print_sleep("what character do you choose? ",1)
    choice = ''
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2.)\n")
        character = choice

def intro():
    print_sleep("You find yourself standing in an open field, filled with grass and yellow wildflowers.", 3)
    print_sleep(f"Rumor has it that a {enemy} is somewhere around here, and has been terrifying the nearby village.", 3)
    print_sleep("In front of you is a house.", 2)
    print_sleep("To your right is a dark cave.", 2)
    print_sleep(f"In your hand you hold your trusty (but not very effective) {weapon}.", 2)

def choose_approach():
    print_sleep("", 1)
    print_sleep("Enter 1 to knock on the door of the house.", 2)
    print_sleep("Enter 2 to peer into the cave.", 2)
    print_sleep("What would you like to do?", 0)
    choice = ''
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2.)\n")

    if choice == '1':
        house()
    elif choice == '2':
        cave()  

def cave():
    global cave_visited    
    global weapon
    print_sleep("You peer cautiously into the cave.", 2)
    if cave_visited:
        print_sleep("You've been here before, and gotten all the good stuff. It's just an empty cave now.", 2)
    elif cave_visited is False:
        print_sleep("It turns out to be only a very small cave.", 2)
        print_sleep("Your eye catches a glint of metal behind a rock.", 2)
        if character == '2':
            print_sleep("You have found Emberfall Daggers!",2)
            print_sleep("Forged in the heart of a dragon's inferno, these twin blades burn with an eternal flame, ready to ignite the battlefield.",2)
            weapon = "Emberfall Daggers" 
        elif character == '1':          
            print_sleep("You have found the Frostheart Scepter!", 2)
            print_sleep("This ancient scepter, once wielded by a forgotten ice deity, pulses with the raw power of glaciers and blizzards.",2)
            weapon = "Frostheart Scepter" 
        print_sleep(f"You discard your silly old dragger and take the {weapon} with you.", 2)
    cave_visited = True
    print_sleep("You walk back out to the field.", 2)
    choose_approach()        

def house():
    print_sleep("You approach the door of the house.", 2)
    print_sleep(f"You are about to knock when the door opens and out steps a {enemy}.", 2)
    print_sleep(f"Eep! This is the {enemy}'s house!", 2)
    combat(weapon)

def combat(weapon):
    print_sleep(f"The {enemy} attacks you!", 2)
    if weapon == "dagger":
        print_sleep(f"You feel a bit under-prepared for this, what with only having a tiny {weapon}.", 2)
    choice = input("Would you like to (1) fight or (2) run away?")
    if choice == '1':
        if weapon == "dagger":
            print_sleep(f"You do your best...", 1)
            print_sleep(f"but your {weapon} is no match for the {enemy}.", 2)
            print_sleep(f"You have been defeated!""", 2)
        else:
            print_sleep(f"As the {enemy} moves to attack, you unsheath your new weapon.", 2)
            print_sleep(f"The {weapon} shines brightly in your hand as you brace yourself for the attack.", 3)
            print_sleep(f"But the {enemy} takes one look at your shiny new toy and runs away!", 3)
            print_sleep(f"You have rid the town of the {enemy}. You are victorious!", 3)
    elif choice == '2':
        print_sleep("You run back into the field. Luckily, you don't seem to have been followed.", 2)
        choose_approach()

def play_again():
    choice = ''
    while choice not in ['y', 'n']:
        choice = input("Would you like to play again? (y/n)")
        if choice == 'n':
            print_sleep("Thanks for playing! See you next time.", 2)
            return 'game_over'
        elif choice == 'y':
            print_sleep("Excellent! Restarting the game ...", 2)
            weapon = 'dagger'
            return 'running'   


state = 'running'
character = ''
while state == 'running':

    enemies = ['troll', 'wicked fairie', 'pirate', 'gorgon', 'dragon']
    enemy = random.choice(enemies)
    weapon = 'dagger'
    cave_visited = False
    choose_character()
    intro()
    choose_approach()
    state = play_again()     
