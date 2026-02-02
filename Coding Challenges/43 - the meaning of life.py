"""
hello reader
click (left or right) to colour in squares
press any key to advance the animation
"""


import pygame
import time
pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((512,512))
grid=[[0 for _ in range(64)] for _ in range(64)]

def get_neighbour_coordinates(y,x): #i gives y, j gives x
    coords=[]
    #aboves
    if y!=0:
        if x!=0:
            coords.append([y-1,x-1])
        coords.append([y-1,x])
        if x!=63:
            coords.append([y-1,x+1])
    #adjacents
    if x!=0:
        coords.append([y,x-1])
    if x!=63:
        coords.append([y,x+1])
    #belows
    if y!=63:
        if x!=0:
            coords.append([y+1,x-1])
        coords.append([y+1,x])
        if x!=63:
            coords.append([y+1,x+1])
    return coords

def count_alives(y,x):
    count=0
    for i in get_neighbour_coordinates(y,x):
        if grid[i[0]][i[1]]==1:
            count+=1
    return count

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
            grid[mouse_pos[1]//8][mouse_pos[0]//8]^=1
            time.sleep(0.1)
        if event.type==pygame.KEYDOWN:
            changes={}
            for i in range(64):
                for j in range(64):
                    count=count_alives(i,j)
                    if count<=1:
                        changes[(i,j)]=0
                    elif grid[i][j]==1 and (count==2 or count==3):
                        changes[(i,j)]=grid[i][j]
                    elif grid[i][j]!=1 and count==3:
                        changes[(i,j)]=1
                    elif grid[i][j]==1 and count>3:
                        changes[(i,j)]=0
            for i in changes:
                grid[i[0]][i[1]]=changes[i]

    #check if a new square is being added

    #check if advancement is to be made

    #render squares
    screen.fill("Black")
    for i in range(64):
        for j in range(64):
            if grid[i][j]==1:
                pygame.draw.rect(screen,"White",pygame.Rect(j*8,i*8,8,8))

    pygame.display.update()
    clock.tick(60)