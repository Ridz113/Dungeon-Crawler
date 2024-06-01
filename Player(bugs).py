from pygame import *

import random

init()

width = 1440
height = 900

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)


class player():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.velocity = 2
        self.Health = 100
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.no_dash_state = False

        self.playerRight = image.load("Player(Right).PNG")
        self.playerRight = transform.scale(self.playerRight, (self.w, self.h))

        self.playerLeft = image.load("Player(Left).PNG")
        self.playerLeft = transform.scale(self.playerLeft, (self.w, self.h))

        self.playerUp = image.load("Player(Up).PNG")
        self.playerUp = transform.scale(self.playerUp, (self.w, self.h))

        self.playerDown = image.load("Player(Down).PNG")
        self.playerDown = transform.scale(self.playerDown, (self.w, self.h))

    def draw(self, screen):
        screen.blit(self.playerRight, (self.x, self.y))



    def moveright(self):
        self.right = True
        self.left = False
        self.down = False
        self.up = False
        if self.right:
            if self.x + 202 < width and self.x > 0:
                self.x = self.x + self.velocity



screen = display.set_mode((width, height))
player = player(100, 100, 192, 202)
display.set_caption('Dungeon Crawler')
endProgram = False

while not endProgram:  # pygame event loop
    for e in event.get():
        if e.type == QUIT:
            endProgram = True

        if e.type == KEYDOWN:
            if e.key == K_RIGHT:
                player.moveright()



    screen.fill(black)
    player.draw(screen)
    display.update()

# bug 1 - player movement - must repeatedly click input button to move player
# fix 1 - Make a new function called update