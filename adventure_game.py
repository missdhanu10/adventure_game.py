import time
import random
items = []


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(0.2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if response == option1:
            break
        elif response == option2:
            break
        else:
            print_pause("Please enter a valid input")
    return response


monster = ["wicked fairie", "dragon", "witch", "ghost", "vampire"]
sel_monster = random.choice(monster)


def intro():
    print_pause("You find yourself standing in an open field,")
    print_pause("filled with grass and yellow wild flowers.")
    print_pause(f"Rumor has it that {sel_monster} is somewhere around here,")
    print_pause("and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                "(but not very effective) dagger.\n")


def play(items):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    response = valid_input("Please enter 1 or 2\n", "1", "2")
    if response == "1":
        house(items)
    elif response == "2":
        cave(items)


def house(items):
    if "sword" in items:
        print_pause("You approach the door of the house.")
        print_pause(f"You are about to knock when the door")
        print_pause(f"opens and out steps a {sel_monster}.")
        print_pause(f"Eep! This is the {sel_monster}'s house!")
        print_pause(f"The {sel_monster} attacks you!")
        response = valid_input("Would you like to (1) fight"
                               "or (2) run away?", "1", "2")
        if response == "1":
            print_pause("As the troll moves to attack,")
            print_pause("you unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in your")
            print_pause("hand as you brace yourself for the attack.")
            print_pause(f"But the {sel_monster} takes one look")
            print_pause("at your shiny new toy and runs away!")
            print_pause(f"You have rid the town of the {sel_monster}.")
            print_pause("You are victorious!")
            play_again()
        elif response == "2":
            print_pause("You run back into the field. Luckily,")
            print_pause("you don't seem to have been followed.\n")
            play(items)
        else:
            print_pause("Please enter a valid input")

    else:
        print_pause("You approach the door of the house.")
        print_pause(f"You are about to knock when the door")
        print_pause(f"opens and out steps a {sel_monster}.")
        print_pause(f"Eep! This is the {sel_monster}'s house!")
        print_pause(f"The {sel_monster} attacks you!")
        print_pause("You feel a bit under-prepared for this")
        print_pause("what with only having a tiny dagger.")
        response = valid_input("Would you like to (1) fight"
                               "or (2) run away?", "1", "2")
        if response == "1":
            print_pause("You do your best...")
            print_pause(f"but your dagger is no match for the {sel_monster}.")
            print_pause("You have been defeated!")
            play_again()
        elif response == "2":
            print_pause("You run back into the field. Luckily,")
            print_pause("you don't seem to have been followed.\n")
            play(items)
        else:
            print_pause("Please enter a valid input")


def cave(items):
    if "sword" in items:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten")
        print_pause("all the good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.\n")
        play(items)
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger")
        print_pause("and take the sword with you.")
        print_pause("You walk back out to the field.\n")
        items.append("sword")
        play(items)


def play_again():
    play_again = valid_input("Would you like to play again?"
                             "(y/n)", "y", "n")
    if play_again == "y":
        print_pause("Excellent! Restarting the game ...")
        global sel_monster
        sel_monster = random.choice(monster)
        play_game()
    elif play_again == "n":
        print_pause("Thanks for playing! See you next time.")


def play_game():
    intro()
    play(items)


play_game()
