# import
import random   # used to generate random numbers for questions


# game setup
health = 3          # player starts with 3 health points
room = 1            # starting room
total_rooms = 5     # number of rooms to escape


# intro
print("Math Dungeon Escape")
print("=====================")
print("Answer math problems to escape the dungeon!")
print("You have 3 health points.\n")


# main game loop
# Runs while player still has health AND hasn't finished all rooms
while room <= total_rooms and health > 0:

    # Generate random numbers for the math problem
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)

    # Randomly choose an operation (+, -, or *)
    operation = random.choice(["+", "-", "*"])


    # calculate correct answer
    if operation == "+":
        correct_answer = num1 + num2
    elif operation == "-":
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2


    # display room + question
    print(f"Room {room}")
    print(f"Solve: {num1} {operation} {num2}")


    # get user input
    # Convert input to an integer so it can be compared
    answer = int(input("Your answer: "))


    # check answers
    if answer == correct_answer:
        # If correct → move to next room
        print("Correct! The door opens.\n")
        room += 1
    else:
        # If wrong → lose health
        health -= 1
        print(f"❌ Wrong! The correct answer was {correct_answer}.")
        print(f"Health left: {health}\n")


# end game
if room > total_rooms:
    print("You escaped the Math Dungeon!")
else:
    print("Game over! The dungeon got you.")