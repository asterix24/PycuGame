#muoviamo sto coso!

bg_file="images/sfondo.bmp"
#ch_file="images/omino.bmp"
import pygame as py
from pygame.locals import*

py.init()

FPS = 30 # frames per second setting
fpsClock = py.time.Clock()

screen=py.display.set_mode((640,480),0,32)
bg=py.image.load(bg_file).convert()
#ch=py.image.load(ch_file)
pycu=py.image.load('images/sheep.png')
puff=py.image.load('images/puff.png')
px=10
#pyi=10
py.draw.rect(bg,(255,0,0),Rect((300,330),(10,80)))
y=298
move_x,move_y=0,0
while True:
    for event in py.event.get():
        if event.type==QUIT:
            exit()
        if event.type==KEYDOWN:
            #if event.key== K_a:
                #move_x=-1
            #elif event.key== K_d:
                #move_x=+1
            if event.key== K_SPACE :
                move_y=-20
            elif event.key== K_0:
                exit()

        elif event.type==KEYUP:
             if event.key== K_a:
                move_x=0
             elif event.key==  K_d:
                move_x=0
             elif event.key== K_SPACE :
                move_y=2.5
    y+=move_y
    px+=3
    if y>298:
        y=298
    elif y<0:
       y=0
    elif y<220:
        y=220
    # non oltre la sbarra! ->>
    if y==298 and px in range(230,240):
            px=230
            pycu=puff
    elif px>240 and y<=298 :
        px=px
    if px >640:
        px = 10

    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    #screen.blit(ch,(x,y))
    screen.blit(pycu,(px,y))
    py.display.update()
    fpsClock.tick(FPS)
'''per far "sparare" prova in event.key== tasto a caso, genera
 un cerchio e lo fa muovere lungo lo schermo'''

