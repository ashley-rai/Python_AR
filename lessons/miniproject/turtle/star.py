import turtle

animal = turtle.Turtle()

animal.shape("turtle")
animal.speed(10)


for i in range(100):
    animal.forward(200)
    animal.left(170)


# animal.hideturtle()
turtle.done()
