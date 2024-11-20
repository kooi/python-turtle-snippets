import turtle
tina = turtle.Turtle()
tina.shape("turtle")

def b(p1, p2, p3, p4, dt=0.01):
    tl = [0 + i * dt for i in range(int(1/dt)+1) ]
    x = []
    y = []
    for t in tl:
        x.append(
            (1-t)**3 * p1[0] +
            3*t*(1-t)**2 * p2[0] +
            3*(t**2)*(1-t) * p3[0] +
            t**3 * p4[0]
        )
        y.append(
            (1-t)**3 * p1[1] +
            3*t*(1-t)**2 * p2[1] +
            3*(t**2)*(1-t) * p3[1] +
            t**3 * p4[1]
        )
    return zip(x, y)


spline = b(
        (  0,   0),
        (  0,  50),
        (150, 100),
        ( 50, 150)
    )
    

tina.penup()
tina.goto(spline[0][0], spline[0][1])
tina.pendown()

for point in spline:
    tina.goto(point[0], point[1])
    
    

