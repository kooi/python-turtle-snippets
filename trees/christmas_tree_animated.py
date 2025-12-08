import turtle
import random

tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(0)
turtle.Screen().tracer(0)


def kerstbal(p):
    kleuren = ["red", "blue", "orange", "purple", "yellow"]
    if random.random() < p:
        tina.pencolor(random.choice(kleuren))
        tina.dot(8)
        tina.pencolor("dark green")

def tree(d, s):
    if d > 0:
        tina.forward(s)
        tree(d-1, s*.8)
        tina.right(120)
        tree(d-3, s*.5)
        tina.right(120)
        tree(d-3, s*.5)
        tina.right(120)
        tina.backward(s)
        kerstbal(0.05)

for i in range(100):

    turtle.Screen().clear()
    tina.goto(0,0)
    tina.pencolor("dark green")
    tina.left(90)
    tina.backward(50)
    tree(15, 50)

    tina.fillcolor("brown")
    tina.backward(10)
    tina.right(90)
    tina.begin_fill()
    for i in range(4):
        tina.forward(15)
        tina.right(90)
        tina.forward(15)
    tina.end_fill()
    turtle.Screen().update()



