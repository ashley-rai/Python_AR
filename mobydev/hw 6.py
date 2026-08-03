# 1 
runningExercise=["jumping jacks","stretching"]
walkingExercise=["pushups","stretching"]

length=len(runningExercise)
print(length)
length=len(walkingExercise)
print(length)

# 2 

subjectsList=["Физика", "Химия", "География"]
print(subjectsList)

first=subjectsList[0]
print(first)

last=subjectsList[-1]
print(last)

subjectsList=["Физика", "Биология", "География"]
print(subjectsList)

#3

person = ["Tom", 35, "New York" ]

name, age, home = person
print(  )
print(name)
print(age)
print(home)


#4

numberList = [1,2,3,4,5]
if 3 in numberList:
    print(  )
    print("Число 3 есть в списке")
else:
    print("Число 3 отсутствует в списке")



#5 

friendsList = ["Sonia","Julia","Renata","Meital"]

if "Abilay" in friendsList:
    print("Мне очень повезло")
else:
    print(  )
    print("Мне не повезло")
    
    
#6

firstList= [1, 2, 3] 
secondList= [1, 2, 4]

if firstList==secondList:
    print(  )
    print( "Списки равны")
else:
    print(  )
    print( "Списки не равны")
    
    
    
    
#7

numbersList = [1,2,3,4,5,6,7,8,9,10]
subList = numbersList[3:7]
print(subList)

#8 
registrationList=[  ] 

registrationList.append("Сара")
registrationList.extend(["Адия","Назар","Амели","Аника"])
print(  )
print(registrationList)
registrationList.insert(2,"Алмас")
print(registrationList)

registrationList[5]="Алуа"
print(registrationList)

deletedItem=registrationList.pop(5)
print(deletedItem)

#9

myWishList=["lego flowers","Lululemon jacket"]
friendsWishList=["Jellycat","dog"]
resultList=myWishList+friendsWishList
print(  )
print(resultList)


#10

gradesList = [
    ["Anna", 35],
    ["Jaden", 40],
    ["Tom", 26]
]

print(gradesList[0])     
print(gradesList[1][0])  
print(gradesList[2][1])  


#11

toyList = ["Car", "Doll", "Ball"]
testToyList = toyList.copy()
testToyList[1] = "Boat"


print("toyList:", toyList)
print("testToyList:", testToyList)

