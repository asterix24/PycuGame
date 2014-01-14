#muoviamo sto coso!

bg_file="images/sfondo.bmp"
#ch_file="images/omino.bmp"
import pygame as py
from pygame.locals import*

py.init()

FPS = 30 # frames per second setting
fpsClock = py.time.Clock()

py.display.set_caption('PyCuGame')
screen=py.display.set_mode((640,480),0,32)
bg=py.image.load(bg_file).convert()
py.draw.rect(bg,(255,0,0),Rect((300,300),(10,80)))

pycu=py.image.load('images/sheep.png')
puff=py.image.load('images/puff.png')
pycua=py.image.load('images/sheep_a.png')
pycub=py.image.load('images/sheep_b.png')

pycu = pycua
a = True
t = 0
px=480
pyi=10
px=10
y=298
move_x,move_y=0,0

while True:
    for event in py.event.get():
        if event.type==QUIT:
            exit()
        if event.type==KEYDOWN:
            if event.key== K_SPACE:
                move_y=-20
            elif event.key == K_ESCAPE:
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

    t += 1
    px -= 5

    if px <= 10:
        px = 480

    if t == 3:
        t = 0
        pycu = pycub
        if a:
            pycu = pycua
        a = not a

    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    screen.blit(pycu,(px,y))

    py.display.update()
    fpsClock.tick(FPS)

'''per far "sparare" prova in event.key== tasto a caso, genera
 un cerchio e lo fa muovere lungo lo schermo'''

