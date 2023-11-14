#import sys
#sys.setExecutionLimit(120000)
import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(0)

def vierkant(x, c):
    tina.penup()
    tina.fillcolor(c)
    tina.begin_fill()
    for i in range(4):
        tina.forward(x)
        tina.right(90)
    tina.end_fill()
    tina.forward(x)
    
palette0 = {
    0: "black",
    1: "white",
    2: "red",
    3: "firebrick",
    4: "dark red",
    5: "light blue",
    6: "dark green",
    7: "green"
}
palette1 = {
    0: "white",
    1: "black",
    2: "red",
    3: "firebrick",
    4: "pink",
    5: "light blue",
    6: "dark green",
    7: "dark red"
}
palette2 = {
    0: "yellow",
    1: "black",
    2: "red",
    3: "firebrick",
    4: "dark red",
    5: "light blue",
    6: "dark green",
    7: "pink"
}
palette3 = {
    0: "white",
    1: "yellow",
    2: "red",
    3: "firebrick",
    4: "dark red",
    5: "light blue",
    6: "dark green",
    7: "pink"
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

kirby = [
        [ 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0 ],
        [ 0, 1, 7, 7, 1, 7, 7, 7, 7, 7, 1, 1, 0, 0, 0, 0 ],
        [ 1, 7, 7, 1, 7, 7, 7, 7, 7, 7, 7, 7, 1, 0, 0, 0 ],
        [ 1, 7, 7, 7, 7, 1, 7, 1, 7, 7, 7, 7, 7, 1, 0, 0 ],
        [ 1, 7, 7, 7, 7, 1, 7, 1, 7, 7, 7, 7, 7, 1, 0, 0 ],
        [ 1, 7, 7, 7, 7, 1, 7, 1, 7, 7, 7, 7, 7, 7, 1, 0 ],
        [ 1, 7, 7, 7, 7, 1, 7, 1, 7, 7, 7, 7, 7, 7, 7, 1 ],
        [ 0, 1, 7, 6, 6, 7, 7, 7, 6, 6, 7, 7, 7, 7, 7, 1 ],
        [ 0, 1, 7, 7, 7, 7, 1, 7, 7, 7, 7, 7, 1, 1, 1, 0 ],
        [ 0, 1, 7, 7, 7, 7, 1, 7, 7, 7, 7, 1, 2, 2, 2, 1 ],
        [ 0, 0, 1, 7, 7, 7, 7, 7, 7, 7, 1, 2, 2, 2, 2, 1 ],
        [ 0, 0, 1, 1, 7, 7, 7, 7, 7, 7, 1, 2, 2, 2, 2, 1 ],
        [ 0, 1, 2, 2, 1, 1, 7, 7, 7, 1, 2, 2, 2, 2, 1, 0 ],
        [ 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 0, 0 ],
        [ 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    ]


def draw_image(img, d, pal):
    for j in img:
        for i in j:
            vierkant(d, pal.get(i))
        tina.backward(len(j)*d)
        tina.right(90)
        tina.forward(d)
        tina.left(90)

size = 10
tina.speed(0)
tina.getscreen().tracer(0)
tina.penup()
tina.goto(-160,160)
tina.pendown()
draw_image(kirby, size, palette0)
draw_image(kirby, size, palette1)
tina.penup()
tina.goto(-160,160)
tina.forward(16*size)
tina.pendown()
draw_image(kirby, size, palette2)
draw_image(kirby, size, palette3)
tina.getscreen().update()
tina.getscreen().exitonclick()
