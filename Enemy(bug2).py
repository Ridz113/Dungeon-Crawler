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
    def __init__(self,x,y,w,h,health,damage,velocity):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.health = health
        self.damage = damage
        self.velocity = velocity
        self.enemycount = random.randint(1,5)
        self.enemy_hitbox = Rect(self.x,self.y,self.w,self.h)

        self.enemyimg = image.load("Enemy.PNG")
        self.enemyimg = transform.scale(self.enemyimg, (self.w, self.h))


    def draw(self,screen):

        screen.blit(self.enemyimg, (self.x, self.y))

class enemyscreen():
    def __init__(self):
        self.enemylist = []

    def generate(self):

        enemy.x = random.randint(10, 1300)
        enemy.y = random.randint(10, 700)
        enemy.health = random.randint(10, 100)
        enemy.damage = random.randint(10, 100)
        enemy.velocity = random.randint(1, 8)

        ghost = enemy(enemy.x, enemy.y, 72, 60,enemy.health,enemy.damage,enemy.velocity)
        print(ghost.enemycount)

        if len(self.enemylist) < ghost.enemycount:
            self.enemylist.append(ghost)
            #print("X co-ord:",ghost.x,"Y Co-ord:",ghost.y)
            #print("Health:",ghost.health,"damage:",ghost.damage,"Velocity:",ghost.velocity)
            #print("")

            enemy.x = random.randint(10, 1300)
            enemy.y = random.randint(10, 700)
            enemy.health = random.randint(10, 100)
            enemy.damage = random.randint(10, 100)
            enemy.velocity = random.randint(1, 8)




screen = display.set_mode((width, height))
display.set_caption('Enemy')
endProgram = False
clock = time.Clock() # Creates a clock using the time library to set FPS

enemyscreen = enemyscreen()

while not endProgram:  # pygame event loop

    clock.tick(60) # Sets FPS to be 60

    for e in event.get():
        if e.type == QUIT:
            endProgram = True

    screen.fill(black)
    enemyscreen.generate()

    for ghost in enemyscreen.enemylist:
        ghost.draw(screen)

    display.update()

# bug 2 - The enemy count variable is not randomnly generated even tho i made it so, it always does the maximum amout of enemies
# fix 2 - Move enemy count variable to eenmy screen class