import pygame
import random
pygame.init()#initializes Pygame
pygame.display.set_caption("It Do Be Breakin' Out")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen
screen.fill((0, 0, 0))#paint background black
doExit = False
clock = pygame.time.Clock()

vx=350

xpos = 5

#balz
bx = 350
by = 250
bVx = 5
bVy = 5

class bick:
    def __init__(self, xpos, ypos ):
        self.xpos = xpos
        self.ypos = ypos
        
    def draw(self):
        pygame.draw.rect(screen, (255, 0, 255), (self.xpos, self.ypos, 70, 20))

bickbag = list()
for i in range(10):
    bickbag.append(bick(xpos,10))
    xpos+=80

#LOP-------------------------------------
while not doExit:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True

    #Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        if vx > 0 and vx < 800 - 200:
            vx+=6
    if keys[pygame.K_LEFT]:
        if vx > 0 and vx < 800 - 200:
            vx-=6

    #LOIGIC------------

    #move Bal
    bx += bVx
    by += bVy

    #releft baz

    if bx < 0 + 10 or bx > 800 - 10:
        bVx *= -1
    if by < 0 + 10 or by > 800 - 10:
        bVy *= -1

    #pattle refect
    if by > 700 - 10 and by < vx + 700 and bx > vx:
        bVy *= -1

    #RENDER SUS----------
    screen.fill((0,0,0))

    pygame.draw.circle(screen,(255, 255, 255),(bx,by),10)

    pygame.draw.rect(screen, (255, 255, 255), (vx, 700, 200, 30))

    for bick in bickbag:
        bick.draw()
    

    pygame.display.flip()
#End Lop--------------------------------

