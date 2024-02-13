import sys
import turtle
import random
import math

sys.setExecutionLimit(60000)

tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(0)
tina.pensize(2)

def branch(len):
    c = (len * 5, 255 - len * 10, 0)
    l = random.randint(15, 15 + math.floor(len))
    r = random.randint(15, 15 + math.floor(len))
    if len < 5:
        return
        
    tina.left(l)
    tina.forward(len)
    tina.pencolor( c )
    branch(len *.75 )
    tina.pencolor( c )
    tina.backward(len)
    tina.right(l)
    
    tina.right(r)
    tina.forward(len)
    tina.pencolor( c )
    branch(len *.80)
    tina.pencolor( c )
    tina.backward(len)
    tina.left(r)


tina.tracer(60)
    
tina.left(90)    

for i in range(100):
    tina.pencolor("brown")
    tina.backward(50)
    tina.forward(50)
    branch(35)    
    tina.pencolor("brown")

tina.backward(50)
