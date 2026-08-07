#1

coloursTuple=("красный", "зеленый", "синий")
print(coloursTuple)

#2
numbersTuple=(1,2,3,4,5)

firstItem=numbersTuple[0]
lastItem=numbersTuple[-1]
print(firstItem)
print(lastItem)

#3

infoTuple=("Иванов", "Иван", 25, "Москва")
ivanAge=infoTuple[2]
print(ivanAge)

#4

tuple1=(1,2,3)
tuple2=(4,5,6)
tuple3=tuple1+tuple2
print(tuple3)

#5
coordinatesTuple= (10, 20, 30, 40)
numbers2= coordinatesTuple[1]
numbers3= coordinatesTuple[2]
print(numbers2)
print(numbers3)

#6

fruitsTuple= ("яблоко", "апельсин", "банан", "апельсин")
index_orange = fruitsTuple.index("апельсин")
print(index_orange)

#7

names=  ("Анна", "Иван", "Мария")
print(names)
if ("Петр") in names:
    print("Петр есть в кортеже")
else:
    print( "Петр отсутствует в кортеже")
    
#8

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
if tuple1 == tuple2:
    print("Кортежи одинаковы")
else:
    print("Кортежи различаются")