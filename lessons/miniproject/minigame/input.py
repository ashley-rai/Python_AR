import random

tries = 3
min = 1
max = 6

randomNum = random.randint(min, max)
instruct = f"  pick a number from {min} to {max} = ".upper()

print()

for i in range(tries):
    try:
        userInput = input(instruct)
        number = int(userInput)
    except:
        if userInput.__contains__("\\"):
            break
        else:
            print("not a number")
            continue

    if number == randomNum:
        print("yay!")
        break
    elif number not in range(min, max + 1):
        print(f"must be between {min} and {max}, try again")
    elif i == tries - 1:
        print("game over")
    else:
        print("guess again")

print()
