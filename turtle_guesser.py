# Code to play guess who but with ninja turtles

import random


class Donny:
    name = "Donatello"
    number = 1
    weapon = "A Bo Staff"
    color = "Purple"
    personality = "critical, scientific & patient"


class Raph:
    name = "Raphael"
    number = 2
    weapon = "A pair of Sais"
    color = "Red"
    personality = "quick to anger, vigilant, perhaps even spicy"


class Leo:
    name = "Leonardo"
    number = 3
    weapon = "Twin Katanas"
    color = "Blue"
    personality = "driven, motivated, considered a leader"


class Mikey:
    name = "Michelangelo"
    number = 4
    weapon = "Nunchucks"
    color = "Orange"
    personality = "warm, funny, a bit of a goof-ball"


# above are the classes holding info for the 4 turtles
playing = True
not_playing = False
# I'll put my methods/functions here to use further down


def play_again():
    not_playing
    print("")
    print("Would you like to play again?")
    a5 = input("yes/no")
    if a5 == "yes":
        question_one()
    else:
        "Thanks for playing."


def question_three():
    turtle3 = random.choice(turtle_list)
    print("Would you describe your Ninja Turtle's Personality as\n"
          + turtle3.personality + "?")
    a4 = input("yes/no")
    if a4 == "yes":
        print("You picked the Ninja Turtle " + turtle3.name + ". Third try is the Charm!")
        play_again()
    elif a4 == "no":
        turtle_list.remove(turtle3)
        turtle4 = random.choice(turtle_list)
        print("You picked the ninja Turtle " + turtle4.name + ". Three guesses. Man I'm smart!")
        play_again()
    elif a4 == "quit":
        quit()
    else:
        print("Incorrect syntax friend. I know spelling three letter words is difficult")
        question_three()


def question_two():
    turtle2 = random.choice(turtle_list)
    print("Does your Ninja Turtle use " + turtle2.weapon + "?")
    a3 = input("yes/no")
    if a3 == "yes":
        print("You picked the Ninja Turtle " + turtle2.name + ". Took two guesses but I got it!")
        play_again()
    elif a3 == "no":
        turtle_list.remove(turtle2)
        question_three()
    elif a3 == "quit":
        quit()
    else:
        print("Incorrect Syntax. Today I'm only taking Yes or No")
        question_two()


def question_one():
    playing
    turtle1 = random.choice(turtle_list)
    print("Does your Ninja Turtle wear the color " + turtle1.color + "?")
    a2 = input("yes/no")
    if a2 == "yes":
        print("You picked the Ninja Turtle " + turtle1.name + " I told you I was good at this!")
        play_again()
    elif a2 == "no":
        turtle_list.remove(turtle1)
        question_two()
    elif a2 == "quit":
        quit()
    else:
        print("Incorrect Syntax. Today I'm only taking Yes or No")
        question_one()


turtle_list = [Donny, Raph, Leo, Mikey]


print("I know everything about the Ninja Turtles!\n"
      "\n"
      "Go ahead and think of one ninja turtle.\n"
      "\n"
      "I bet ya, I can guess which turtle you picked in 3 or less guesses!\n"
      "Please, answer any questions with a yes/no. Type 'quit' to leave")

print("Are you ready to begin?")
a1 = input("yes/no")
if a1 == "yes":
    question_one()
elif a1 == "quit":
    quit()
else:
    print("Let's try again another time")
