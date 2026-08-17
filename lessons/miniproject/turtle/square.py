import turtle

animal = turtle.Turtle()

animal.shape("turtle")
# animal.speed(1)


def square(side: float):
    for i in range(4):
        animal.forward(side)
        if i != 3:
            animal.left(90)


square(side=10)

# animal.hideturtle()
turtle.done()
