import sys
sys.setExecutionLimit(120000)
import turtle
tina = turtle.Turtle()
tina.shape("turtle")

def vierkant(x, c):
    tina.penup()
    tina.fillcolor(c)
    tina.begin_fill()
    for i in range(4):
        tina.forward(x)
        tina.right(90)
    tina.end_fill()
    tina.forward(x)
    
palette = {
    0: "white",
    1: "black",
    2: "red",
    3: "firebrick",
    4: "dark red",
    5: "light blue",
    6: "blue"
}
    
red_guy = [
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 1, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0 ],
        [ 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0 ],
        [ 0, 1, 5, 0, 5, 6, 1, 2, 2, 2, 1, 2, 2, 1, 0, 0 ],
        [ 0, 1, 6, 6, 6, 6, 1, 2, 2, 2, 1, 3, 3, 1, 0, 0 ],
        [ 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 1, 3, 3, 1, 0, 0 ],
        [ 0, 0, 1, 3, 3, 2, 2, 2, 3, 3, 1, 3, 3, 1, 0, 0 ],
        [ 0, 0, 1, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 1, 0, 0 ],
        [ 0, 0, 1, 3, 3, 3, 1, 3, 3, 3, 1, 4, 4, 1, 0, 0 ],
        [ 0, 0, 1, 3, 3, 1, 0, 1, 3, 3, 1, 1, 1, 0, 0, 0 ],
        [ 0, 0, 1, 3, 3, 1, 0, 1, 3, 3, 1, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0 ]
    ]


def draw_image(img, d):
    for j in img:
        for i in j:
            vierkant(d, palette.get(i))
        tina.backward(len(j)*d)
        tina.right(90)
        tina.forward(d)
        tina.left(90)

tina.speed(0)
#tina.getscreen().tracer(0)
tina.penup()
tina.goto(-200,200)
tina.pendown()
draw_image(red_guy, 20)
#tina.getscreen().update()
