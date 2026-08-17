import turtle

animal = turtle.Turtle()
animal.shape("turtle")
# animal.speed(1)
animal.color("red", "blue")


def triangle(side: float):
    animal.begin_fill()
    for i in range(3):
        animal.forward(side)
        if i != 2:
            animal.left(120)
    animal.end_fill()


triangle(200)
triangle(200)
triangle(200)

animal.penup()
animal.goto(0, 100)


turtle.done()
