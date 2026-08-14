from functions import printNum

printNum(1)

for _ in range(1, 8):
    print("Python")


printNum(2)

productList = ["Хлеб", "Молоко", "Яйца", "Картофель"]

for product in productList:
    print(f"Я купил {product}")


printNum(3)

companyName = "MobyDev"

for index, letter in enumerate(companyName):
    print(f"{index}: {letter}")


companyName = "MobyDev"

for index, letter in enumerate(companyName):
    print(f"{index}: {letter}")


printNum(4)

playerProgressDict = {
    "Don": 102,
    "Tomas": 98,
    "Riki": 48,
    "Lora": 153,
    "Vladislav": 200,
}

for key, value in playerProgressDict.items():
    if value > 100:
        print(f"Игрок {key}, достиг следующего уровня")
    else:
        print(f"Игрок {key} не достиг следующего уровня")


printNum(5)

potatoCount = int(input("Введите кол-во картошки: "))

while potatoCount > 0:
    print("Почистил")
    potatoCount -= 1
    print(f"В мешке осталось {potatoCount}")


printNum(6)

import random

cubeValue = random.randint(1, 6)

while cubeValue != 1:
    print(cubeValue)
    cubeValue = random.randint(1, 6)

print(cubeValue)


printNum(7)


correctPassword = "admin123"

userPassword = input("Введите пароль: ")

while userPassword != correctPassword:
    userPassword = input("Попробуйте еще раз: ")

print("Вы успешно авторизовались!")
