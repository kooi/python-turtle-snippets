from math import sin, cos
import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(0)
tina.getscreen().tracer(10)

t = 0
dt = 0.01

spiro = [
    {
        'r': 100.0,
        'f': 0.5,
        'p': 0.5
    },
    {
        'r': 50.0,
        'f': 3.0,
        'p': 0
    },
#    {
#        'r': 10.0,
#        'f': 15.0,
#        'p': 0
#    }
]

def pos(s, t):
    x = 0
    y = 0
    for node in s:
        x = x + node['r']*cos(t * node['f'] - node['p'])
        y = y + node['r']*sin(t * node['f'] - node['p'])
    return x, y


tina.penup()
tina.goto( pos(spiro, 0) )
tina.pendown()


while True:
    tina.goto(pos(spiro, t))
    t = t + dt
