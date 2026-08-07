#1

monthDict={"Январь": 31,
           "Февраль": 28,
           "Март": 31,
           }
print(monthDict)

monthDict["Апрель"] = 30
print(monthDict)
monthDict["Февраль"] = 29
print(monthDict)

#2

tempDict = {
    "Easy": 10,
    "Medium": 8,
    "Fast": 6
}
print(   )
print("Исходный словарь:", tempDict)

tempDict["Sprint"] = 4
print("После добавления Sprint:", tempDict)

if "Sprint" in tempDict:
    tempDict["Sprint"] = 3.8
else:
    print("Ключ 'Sprint' не найден в словаре.")
print("После изменения значения Sprint:", tempDict)
deletedTemp = tempDict.pop("Sprint", None)
print("Удаленное значение (deletedTemp):", deletedTemp)
print(f"Рекомендую Вам бежать с темпом {tempDict['Medium']} минут на километр")

#3

sportInventoryDict = {
"Мяч" : 20,
"Скакалка" : 10,
"Ракетка" : 12,
"Секундомер": 2
}
print(  )
print("Ключи словаря (наименования инвентаря):", sportInventoryDict.keys())
sportInventoryDict["Мяч"] = 18
sportInventoryDict["Ракетка"] = 11
print("Значения словаря (количество инвентаря):", sportInventoryDict.values())

sportInventoryDict2 = {
    "Мяч": 10,
    "Скакалка": 22,
    "Ракетка": 15,
    "Секундомер": 1,
    "Волейбольная сетка": 1
}
sportInventoryDict.update(sportInventoryDict2)
print("Обновленный словарь инвентаря:", sportInventoryDict)

#4

fruitsDict=fruitsDict = {
    "яблоко": "красное",
    "груша": "зеленое",
    "апельсин": "оранжевое"
}
if "груша" in fruitsDict:
    print(    )
    print("Груша есть в словаре")
else:
    print("Груша отсутствует в словаре")
    
    #5
    
personDict1 = {
    "имя": "Анна",
    "возраст": 25
}
personDict2 = personDict1.copy()
personDict2["возраст"] = 30
print(   )
print("personDict1:", personDict1)
print("personDict2:", personDict2)