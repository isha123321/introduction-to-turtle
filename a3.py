import turtle
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(300,400)
turtle.Screen().title("turtle")
my_pen=turtle.Turtle()
size=0
while True:
    for i in range(4):
        my_pen.forward(size+1)
        my_pen.left(90)
        size=size-5
    size=size+1

turtle.done()