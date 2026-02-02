#i'm pretty pleased with this one. if you want to learn how its done look uper polar coordinates :)

#IMPORT-ZONE-------------------------------------------------
import pygame
import math
import random
from sys import exit

#INITALISATION-----------------------------------------------
name="galaxy"
pygame.init()
screen=pygame.display.set_mode((800,800))
pygame.display.set_caption(name)
clock=pygame.time.Clock()

iterations=8000
random_stars=500
a=0.7
theta=0

for i in range(random_stars):
    x=random.randint(0,799)
    y=random.randint(0,799)
    pixel=pygame.Rect(x,y,1,1)
    pygame.draw.rect(screen,"white",pixel)


for i in range(iterations):
    #generate polar coordinates using polar equation
    theta=(i*0.005*math.pi)
    r=a*(theta**1.3)*((-1)**math.floor(theta))
    #convert polar coordinates (r,theta) to cartesian with some randomisation
    noise=max(4,i//600)
    x=int(r*math.cos(theta))+400+random.randint(-1*noise,1*noise)
    y=int(r*math.sin(theta))+400+random.randint(-1*noise,1*noise)
    c=255-int((225*i)/8000)
    colour=pygame.Color(c,c,200)
    if not(y>799 or y<0 or x>799 or x<0):
        pixel=pygame.Rect(x,y,1,1)
        pygame.draw.rect(screen,colour,pixel)

#CLASSES-----------------------------------------------------


#PROCESS-----------------------------------------------------
while True:
    #-THE-INPUT-ZONE-----------------------------------------
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    #DRAWING-------------------------------------------------

    #WINDOW-UPDATING-----------------------------------------
    pygame.display.update()
    clock.tick(60)
