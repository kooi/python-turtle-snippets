import turtle
tina = turtle.Turtle()
tina.shape("turtle")

def b4(path, dt=0.01):
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

def do_click(x,y):
    global path
    path.append( (x,y) )
        
    if len(path) == 4:
        spline = b4(path)
    
        tina.penup()
        tina.goto(spline[0][0], spline[0][1])
        tina.pendown()

        for point in spline:
            tina.goto(point[0], point[1])
            
        path = []

tina.getscreen().onclick(do_click)

