import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(0)

import random
import time

PALETTE = [
            (1, 0, 0), # dood
            (0, 0, 0), # levend
            (1, 1, 1), # achtergrond
          ]

PIXEL_SIZE = 30
PIXEL_MARGIN = 5
GRID_SIZE_X = 10
GRID_SIZE_Y = 10

petridish = [[random.randint(0,1) for x in range(GRID_SIZE_X)]
                  for y in range(GRID_SIZE_Y)]

done = False
#tina.getscreen().tracer(0)

def square(c):
    tina.fillcolor(c)
    tina.begin_fill()
    for i in range(4):
        tina.forward(PIXEL_SIZE)
        tina.right(90)
    tina.end_fill()

while not done:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            done = True
#        elif event.type == pygame.MOUSEBUTTONDOWN:
#            pos = pygame.mouse.get_pos()
#            col = pos[0] // (PIXEL_SIZE+PIXEL_MARGIN)
#            row = pos[1] // (PIXEL_SIZE+PIXEL_MARGIN)
#            petridish[row][col] = 1
#            print("mouseclick(", pos, ") -> (", row,",", col, ")")

    tina.getscreen().bgcolor( PALETTE[2] )
    
    tina.goto(-200,200)
    for j in range(GRID_SIZE_Y):
        for i in range(GRID_SIZE_X):
            square(PALETTE[petridish[j][i]])
            tina.forward(PIXEL_SIZE+PIXEL_MARGIN)
        tina.backward(GRID_SIZE_X * (PIXEL_SIZE+PIXEL_MARGIN) )
        tina.right(90)
        tina.forward(PIXEL_SIZE+PIXEL_MARGIN)
        tina.left(90)
#            pygame.draw.rect( screen, PALETTE[petridish[j][i]],
#                [(PIXEL_SIZE + PIXEL_MARGIN)*i + PIXEL_MARGIN,
#                 (PIXEL_SIZE + PIXEL_MARGIN)*j + PIXEL_MARGIN,
#                 PIXEL_SIZE, PIXEL_SIZE] )
    
#    tina.getscreen().update()
#    time.sleep(1.0/60)


