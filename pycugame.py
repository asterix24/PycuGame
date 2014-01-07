#muoviamo sto coso!

bg_file="images/sfondo.bmp"
ch_file="images/omino.bmp"

import pygame as py
from pygame.locals import*
py.init()
screen=py.display.set_mode((640,480),0,32)
bg=py.image.load(bg_file).convert()
ch=py.image.load(ch_file)
#py.draw.rect(screen,(255,255,255),Rect((300,300),10))
x,y=0,298
move_x,move_y=0,0
while True:
    for event in py.event.get():
        if event.type==QUIT:
            exit()
        if event.type==KEYDOWN:
            if event.key== K_a:
                move_x=-1
            elif event.key== K_d:
                move_x=+1
            elif event.key== K_SPACE :
                move_y=-10
            elif event.key== K_0:
                exit()

        elif event.type==KEYUP:
             if event.key== K_a:
                move_x=0
             elif event.key==  K_d:
                move_x=0
             elif event.key== K_SPACE :
                move_y=2.5
    x+=move_x
    y+=move_y
    if y>298:
        y=298
    elif y<0:
       y=0
    elif y<220:
        y=220
    if x>640:
        x=-20
    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    screen.blit(ch,(x,y))
    py.display.update()
'''per far "sparare" prova in event.key== tasto a caso, genera
 un cerchio e lo fa muovere lungo lo schermo'''

