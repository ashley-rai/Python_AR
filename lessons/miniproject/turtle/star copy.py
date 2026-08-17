import turtle

animal = turtle.Turtle()

animal.shape("turtle")
# animal.speed(10)


for i in range(150):
    animal.forward(i*10)
    animal.left(60 - i / 2)


# animal.hideturtle()
turtle.done()
