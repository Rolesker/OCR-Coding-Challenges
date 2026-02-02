import turtle
import random

while True:
    rotation=[90,180,270,360][random.randint(0,3)]
    if rotation<=180:
        turtle.right(rotation)
    else:
        turtle.left(360-rotation)
    turtle.forward(25)
