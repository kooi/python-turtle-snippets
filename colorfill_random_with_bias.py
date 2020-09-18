import turtle
from random import random

tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(0)

def random_color(w_r=1.0, b_r=0.0, w_g=1.0, b_g=0.0, w_b=1.0, b_b=0.0):
    if w_r + b_r > 1.0:
        w_r = 1.0 - b_r
    if w_g + b_g > 1.0:
        w_g = 1.0 - b_g
    if w_b + b_b > 1.0:
        w_b = 1.0 - b_b
    return (
        random()*w_r+b_r, 
        random()*w_g+b_g, 
        random()*w_b+b_b
    )

def maaknhoek(n):
    for i in range(n):
        tina.right(360./n)
        tina.forward(100)


for j in range(1, 10, 2):
    n = 1000
    tina.getscreen().tracer(0)
    for i in range(n):
        tina.pencolor(random_color(b_b=j/10.0))
        maaknhoek(j)
        tina.left(360.0/n)
    tina.getscreen().update()
    
