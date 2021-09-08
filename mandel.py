import turtle
#from tqdm import tqdm
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(0)
#tina.getscreen().setup(width=350, height=200, startx=None, starty=None)
tina.getscreen().tracer(0)

re_min = -2.5
re_max = 1.0
im_min = -1.0
im_max = 1.0

RES = 0.01

re_num = int((re_max - re_min) / RES)
im_num = int((im_max - im_min) / RES)

def rgb_to_hsv(R, G, B):
    var_R = R
    var_G = G
    var_B = B

    var_Min = min( var_R, var_G, var_B )
    var_Max = max( var_R, var_G, var_B )
    del_Max = var_Max - var_Min 

    V = var_Max

    if ( del_Max == 0 ):
        H = 0
        S = 0
    else:
        S = del_Max / var_Max

    del_R = ( ( ( var_Max - var_R ) / 6 ) + ( del_Max / 2 ) ) / del_Max
    del_G = ( ( ( var_Max - var_G ) / 6 ) + ( del_Max / 2 ) ) / del_Max
    del_B = ( ( ( var_Max - var_B ) / 6 ) + ( del_Max / 2 ) ) / del_Max

    if      ( var_R == var_Max ):
        H = del_B - del_G
    elif ( var_G == var_Max ):
        H = ( 1 / 3 ) + del_R - del_B
    elif ( var_B == var_Max ):
        H = ( 2 / 3 ) + del_G - del_R

    if ( H < 0 ):
        H += 1
    if ( H > 1 ):
        H -= 1


def mandel_iter(a0, b0):
    an = a0
    bn = b0
    for i in range(10):
        an_ = an*an - bn*bn + a0
        bn_ = 2*an*bn + b0
        if an_*an_+bn_*bn_ > 1:
            return i*25
        else:
            an = an_
            bn = bn_
    return 255

#requires tqdm for progress bar
#for j in tqdm(range(im_num)):
for j in range(im_num):
    for i in range(re_num):
        tina.penup()
        tina.goto(i*1 - 200, j*1 - 200)
        c = mandel_iter(i*RES + re_min, j*RES + im_min) / 255.0
        tina.pencolor( 1.0 - c, c, 0)
        tina.dot(1)

#tina.getscreen().exitonclick()
