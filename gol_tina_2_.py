import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(0)

import random
import time
import math

PALETTE = [
            (0, 0, 0), # dood
            (255, 255, 255), # levend
            (128, 128, 128), # achtergrond
          ]

PIXEL_SIZE = 30
PIXEL_MARGIN = 5
GRID_SIZE_X = 10
GRID_SIZE_Y = 10


def count_neighbours(x, y):
  n = 0
  for j in [-1,0,1]:
      for i in  [-1,0,1]:
        if not (j == 0 and i == 0):
          n = n + petridish[(y+j)%GRID_SIZE_Y][(x+i)%GRID_SIZE_X]
  return n


def evolve():
  npd = [[0 for x in range(GRID_SIZE_X)] for y in range(GRID_SIZE_Y)]
  for j in range(GRID_SIZE_Y):
      for i in range(GRID_SIZE_X):
          n = count_neighbours(i,j)
          a = petridish[j][i]

          # 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation
          if a == 1 and n < 2:
            npd[j][i] = 0

          # 2. Any live cell with two or three live neighbours lives on to the next generation
          if a == 1 and (n == 2 or n == 3):
            npd[j][i] = 1

          # 3. Any live cell with more than three live neighbours dies, as if by overpopulation
          if a == 1 and n > 3:
            npd[j][i] = 0

          # 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction
          if a == 0 and n == 3:
            npd[j][i] = 1
  return npd


def square(c):
    tina.fillcolor(c)
    tina.begin_fill()
    for i in range(4):
        tina.forward(PIXEL_SIZE)
        tina.right(90)
    tina.end_fill()


def click(x, y):
    i = x_to_i(x)
    j = y_to_j(y)
    petridish[j][i] = 1 - petridish[j][i]


def x_to_i(x):
    tx = x + (GRID_SIZE_X/2)*(PIXEL_SIZE+PIXEL_MARGIN)
    tx = tx / (PIXEL_SIZE+PIXEL_MARGIN)
    return int(math.floor(tx))


def y_to_j(y):
    ty = y + (GRID_SIZE_Y/2)*(PIXEL_SIZE+PIXEL_MARGIN)
    ty = ty / (PIXEL_SIZE+PIXEL_MARGIN)
    return int(GRID_SIZE_Y - math.floor(ty) - 1)

turtle.Screen().onscreenclick(click)
turtle.Screen().tracer(0)

petridish = [[1 if random.random() > .8 else 0 for x in range(GRID_SIZE_X)] for y in range(GRID_SIZE_Y)]

while True:
  turtle.Screen().bgcolor( PALETTE[2] )

  tina.goto(-(GRID_SIZE_X/2)*(PIXEL_SIZE+PIXEL_MARGIN) , (GRID_SIZE_Y/2)*(PIXEL_SIZE+PIXEL_MARGIN))
  for j in range(GRID_SIZE_Y):
      for i in range(GRID_SIZE_X):
          square(PALETTE[petridish[j][i]])
          tina.penup()
          tina.forward(PIXEL_SIZE+PIXEL_MARGIN)
          tina.pendown()
      tina.penup()
      tina.backward(GRID_SIZE_X * (PIXEL_SIZE+PIXEL_MARGIN) )
      tina.right(90)
      tina.forward(PIXEL_SIZE+PIXEL_MARGIN)
      tina.left(90)
      tina.pendown()

  petridish = evolve()
  time.sleep(1.0/10)
  turtle.Screen().update()
