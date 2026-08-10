#1

animalSet={"Penguin", "Lion", "Zebra", "Giraffe", "Hippopotamus", "Penguin"}
print(animalSet)

# в консоль вывелся только один пенгвин потому что это единственое отличие 
#между множествами и словарями 


#2
registrationSet=set()
registrationSet.add("Сара")

print(registrationSet)

registrationSet.add("Алмас")
print(registrationSet)

registrationSet.pop() # нечего не изменилось
deletedItem={"Сара","Алмас"}
print(deletedItem)
# 3

lettersSet={"a", "b", "c", "d"}
lettersSet.remove("c")
print(lettersSet)

# я использывала метод "remove" потомучто он переводиться с русского как удалить.


# 4

basketBallExerciseSet={"jumping jacks","high knees","stretching arms"}
volleyBallExersicceSet={"stretching","running","high knees"}
generalExercises=basketBallExerciseSet.intersection(volleyBallExersicceSet)

print(generalExercises)

specialExercises=basketBallExerciseSet.difference(volleyBallExersicceSet)
print(specialExercises)


allExercises=basketBallExerciseSet.union(volleyBallExersicceSet)
print(allExercises)

# 5
numbersSet={1, 2, 3, 4, 5}
subNumbersSet={2,4}
if numbersSet.issubset(subNumbersSet):
    print("Это подмножество")
else:
    print( "Это не подмножество")
    
    
    #6
    
numbersList= [1, 2, 3, 2, 4, 5, 3]
numbersSet=set(numbersList)
print(list(numbersSet))






































