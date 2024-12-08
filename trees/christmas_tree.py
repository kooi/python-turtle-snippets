import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(0)
#tina.getscreen().tracer(0)


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

tina.pencolor("dark green")
tina.left(90)
tina.backward(50)
tree(15, 50)
#tina.getscreen().update()



