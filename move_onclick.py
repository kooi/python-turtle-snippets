import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(0)

def do_click(x,y):
    tina.goto(x,y)

turtle.Screen().onclick(do_click)
