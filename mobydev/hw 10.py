from functions import printNum

printNum(1)


def introduceMyself(name: str, age: int):
    print("Hello, my name is " + name + " and I am " + str(age))


introduceMyself("Assylay", age=12)

printNum(2)


def sayHello(name: str):
    print(f"Hello, {name}")


sayHello("Vladislav")
sayHello("Amine")
sayHello("Daniil")

printNum(3)


def introduction(name: str, home: str, age: int):
    print(f"{name}, {age} года, город {home}")


introduction("Олжас", "Алматы", 34)

printNum(4)


def progressUpdate(steps: int, goal: int):
    percentOfGoal = steps / goal * 100
    print(percentOfGoal)

    if percentOfGoal < 10:
        print("У вас хорошее начало")
    elif percentOfGoal < 50:
        print("Вы почти на полпути!")
    elif percentOfGoal < 90:
        print("Вы на полпути!")
    elif percentOfGoal < 100:
        print("Вы почти у цели!")
    else:
        print("Вы превзошли свою цель!")


progressUpdate(2, 2)
progressUpdate(6, 221)
progressUpdate(25, 52)


printNum(5)

def multiply(a, b):
    return a * b

print(multiply(5, 3))
 

printNum(6)


def playerRegistration(nickName="unnamed", race="goblin"):
    if nickName == "unnamed":
        print(f"Твоя раса {race}, но имя еще не определено")
    else:
        print(f"Регистрация пройдена! Добро пожаловать на поля сражений, {nickName} из расы {race}")


playerRegistration()

playerRegistration("Aragorn", "elf")
playerRegistration("Grom", "orc")
playerRegistration(race="vampire")
playerRegistration("Legolas")