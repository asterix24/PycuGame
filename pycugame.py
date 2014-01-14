#muoviamo sto coso!

bg_file="images/sfondo.bmp"
ch_file="images/omino.bmp"

import pygame as py
from pygame.locals import*

py.init()

FPS = 30 # frames per second setting
fpsClock = py.time.Clock()

py.display.set_caption('PyCuGame')
screen=py.display.set_mode((640,480),0,32)
bg=py.image.load(bg_file).convert()
ch=py.image.load(ch_file)
pycu=py.image.load('images/sheep.png')
px=10
pyi=10
py.draw.rect(bg,(255,0,0),Rect((300,300),(10,80)))
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
    # non oltre la sbarra! ->>
    if y==298 and x in range(230,240):
            x=230
    elif x>240 and y<=298 :
        x+=move_x



    px += 5
    if px >= 480:
        px = 10

    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    screen.blit(ch,(x,y))
    screen.blit(pycu,(px,pyi))
    py.display.update()
    fpsClock.tick(FPS)

'''per far "sparare" prova in event.key== tasto a caso, genera
 un cerchio e lo fa muovere lungo lo schermo'''

