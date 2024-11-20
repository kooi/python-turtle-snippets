import turtle
import random
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(0)

def b4(path, dt=0.02):
    if len(path) != 4:
        return path
    tl = [0 + i * dt for i in range(int(1/dt)+1) ]
    x = []
    y = []
    for t in tl:
        x.append(
            (1-t)**3 * path[0][0] +
            3*t*(1-t)**2 * path[1][0] +
            3*(t**2)*(1-t) * path[2][0] +
            t**3 * path[3][0]
        )
        y.append(
            (1-t)**3 * path[0][1] +
            3*t*(1-t)**2 * path[1][1] +
            3*(t**2)*(1-t) * path[2][1] +
            t**3 * path[3][1]
        )
    return zip(x, y)

path = []
r = random.random()
g = random.random()
b = random.random()
Dr = 0.2
Dg = 0.05
Db = 0.1

def do_click(x,y):
    global path, r, g, b
    path.append( (x,y) )
        
    if len(path) == 4:
        spline = b4(path)
    
        tina.penup()
        tina.goto(spline[0][0], spline[0][1])
        tina.pendown()

        for point in spline:
            dr = 2*Dr*random.random()-Dr
            r = r + dr if r + dr < 1.0 else r - dr
            dg = 2*Dg*random.random()-Dg
            g = g + dg if g + dg < 1.0 else g - dg
            db = 2*Db*random.random()-Db
            b = b + db if b + db < 1.0 else b - db
            tina.pencolor(r, g, b)
            tina.goto(point[0], point[1])
            
        path = []

x = random.randint(-200,200)
y = random.randint(-200,200)

while True:
    
    do_click(x, y)
    for i in range(3):
        x = random.randint(-200,200)
        y = random.randint(-200,200)
        do_click( x, y )
 
        
        
