from pygame import *

import random

init()

width = 1440
height = 900

red = (255, 0, 0)
green = (0, 255, 0)
healthbar_green = (42,234,46) # Green for the healthbar
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)


class enemy():
    def __init__(self,w,h):
        self.x = random.randint(10, 1300)
        self.y = random.randint(10, 700)
        self.w = w
        self.h = h
        self.health = random.randint(10,100)
        self.damage = random.randint(10,100)
        self.velocity = random.randint(1,8)
        self.enemycount = 5
        self.enemy_hitbox = Rect(self.x,self.y,self.w,self.h)
        self.enemylist = []
        self.enemyimg = image.load("Enemy.PNG")
        self.enemyimg = transform.scale(self.enemyimg, (self.w, self.h))


    def draw(self,screen):
            screen.blit(self.enemyimg, (self.x, self.y))

    def generate(self):

        if len(self.enemylist) < self.enemycount:
            self.enemylist.append(ghost)

            self.x = random.randint(10, 1300)
            self.y = random.randint(10, 700)








screen = display.set_mode((width, height))
display.set_caption('Enemy')
endProgram = False
clock = time.Clock() # Creates a clock using the time library to set FPS

ghost = enemy(128, 128)

while not endProgram:  # pygame event loop

    clock.tick(60) # Sets FPS to be 60

    for e in event.get():
        if e.type == QUIT:
            endProgram = True

    screen.fill(black)
    ghost.generate()

    for ghost in ghost.enemylist:
        ghost.draw(screen)

    display.update()

# bug 1 - drawing enemies - all enemies mapped to same co-ordinates
# fix 1 - put array in enemy screen and generate enemies in there aswell