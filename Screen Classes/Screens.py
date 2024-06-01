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


class abstractscreen():
    def __init__(self):
        pass

    def handleMouseInput(self, pos):
        for b in self.listOfButtons:
            b.checkClick(pos)


class mainmenu(abstractscreen):

    def __init__(self):
        self.startbutton = image.load("startbutton.PNG")
        self.quitbutton = image.load("quitbutton.PNG")
        self.instructionbutton = image.load("howtoplaybutton.PNG")

        self.b1 = button(100, 700, 200, 100, self.startbutton)  # button (x,y,width,height,image)

        self.b2 = button(500, 700, 300, 105, self.quitbutton)  # button (x,y,width,height,image)

        self.b3 = button(1000, 700, 250, 100, self.instructionbutton)  # button (x,y,width,height,image)

        self.b1.setCallback(self.loadgame)
        self.b2.setCallback(self.quitgame)
        self.b3.setCallback(self.viewinstructions)

        self.listOfButtons = [self.b1, self.b2, self.b3]

    def drawscreen(self, screen):
        self.backgroundimg = image.load("dungeonbg.jpg")
        self.backgroundimg = transform.scale(self.backgroundimg, (width, height))
        screen.blit(self.backgroundimg, (0, 0))

        for b in self.listOfButtons:
            b.draw(screen)

    def loadgame(self):
        global currentScreen
        currentScreen = spawn

        print("Game Loaded")

    def quitgame(self):
        print("Game over")
        exit()

    def viewinstructions(self):
        global currentScreen
        currentScreen = instructionscreen


class instructionmenu(abstractscreen):
    def __init__(self):
        self.backbutton = image.load("backbutton.PNG")
        self.b1 = button(1200, 0, 200, 100, self.backbutton)  # button (x,y,width,height,image
        self.b1.setCallback(self.backtomain)
        self.listOfButtons = [self.b1]

    def drawscreen(self, screen):
        self.instructions = image.load("instructions.png")
        self.instructions = transform.scale(self.instructions, (width, height))
        screen.fill(black)
        screen.blit(self.instructions, (0, 0))

        for b in self.listOfButtons:
            b.draw(screen)

    def backtomain(self):
        global currentScreen
        currentScreen = menuscreen
        print("Menu loaded")


class gamescreen(abstractscreen):
    def __init__(self, colour):
        self.listOfButtons = []
        self.colour = colour

    def drawscreen(self, screen):
        screen.fill(black)
        self.topwall = draw.rect(screen, self.colour, Rect(0, 0, width, 20))  # drawing a rectangle (x,y,width,height)
        self.rightwall = draw.rect(screen, self.colour,Rect(width - 20, 0, 20, height))  # drawing a rectangle (x,y,width,height)
        self.leftwall = draw.rect(screen, self.colour, Rect(0, 0, 20, height))  # drawing a rectangle (x,y,width,height)
        self.bottomwall = draw.rect(screen, self.colour,Rect(0, height - 70, width, 20))  # drawing a rectangle (x,y,width,height)

        self.door = doors()
        self.door.drawdoor(screen)


class enemyscreen(gamescreen):
    pass

class spawnscreen(gamescreen):
    pass


class doors():
    def __init__(self):
        pass

    def drawdoor(self, screen):
        self.topdoor = draw.rect(screen, black,Rect((width / 2) - 100, 0, 200, 20))  # drawing a rectangle (x,y,width,height)
        self.rightdoor = draw.rect(screen, black, Rect(width - 20, (height / 2) - 100, 20,200))  # drawing a rectangle (x,y,width,height)
        self.leftdoor = draw.rect(screen, black,Rect(0, (height / 2) - 100, 20, 200))  # drawing a rectangle (x,y,width,height)
        self.bottomdoor = draw.rect(screen, black, Rect((width / 2) - 100, height - 70, 200,20))  # drawing a rectangle (x,y,width,height)

class button():
    def __init__(self, x, y, w, h, image):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen):
        self.buttonimg = self.image
        self.buttonimg = transform.scale(self.buttonimg, (self.w, self.h))
        screen.blit(self.buttonimg, (self.x, self.y))

    def setCallback(self, callback):
        self.callback = callback

    def checkClick(self, pos):
        if self.rect.collidepoint(pos):
            self.callback()


class dungeon():
    def __init__(self):  #
        self.map = [[0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]]

        self.spawnpointx = random.randint(0, 2)
        self.spawnpointy = random.randint(0, 2)
        self.playerlocationx = self.spawnpointx
        self.playerlocationy = self.spawnpointy
        self.enemy_room = random.randint(1, 2)

    def generatemap(self):
        posx = 0
        posy = 0
        while posx < 5 and posy < 5:
            self.map[posx][posy] = "R"
            posx = posx + 1
            while posx == 5:
                posx = 0
                posy = posy + 1

        posx = 0
        posy = 0

        while posx < 5 and posy < 5:
            if self.enemy_room == 2:
                self.map[posx][posy] = "E"
            self.enemy_room = random.randint(1, 2)
            posx = posx + 1
            while posx == 5:
                posx = 0
                posy = posy + 1

        self.map[self.spawnpointy][self.spawnpointx] = "S"

        return self.map

    def display(self):
        i = 0
        while i < len(self.map):
            print(self.map[i])
            i += 1

    def findlocation(self):
        print("You are in the coordinates:", "(", self.playerlocationx, ",", self.playerlocationy, ")", "Your are in:",
              self.map[self.playerlocationy][self.playerlocationx])

        self.display()
        print("")

    def moveright(self):
        global currentScreen

        print("You have moved right")
        self.playerlocationx += 1

        if Dungeon.playerlocationx > 4:
            Dungeon.playerlocationx = 4
            print("No room there")

        if self.map[Dungeon.playerlocationy][Dungeon.playerlocationx] == "R":
            currentScreen = room
        if self.map[Dungeon.playerlocationy][Dungeon.playerlocationx] == "E":
            currentScreen = enemyroom
        if self.map[Dungeon.playerlocationy][Dungeon.playerlocationx] == "S":
            currentScreen = spawn

        self.findlocation()

    def moveleft(self):
        global currentScreen

        print("You have moved left")
        self.playerlocationx -= 1

        if Dungeon.playerlocationx < 0:
            Dungeon.playerlocationx = 0
            print("No room there")

        if self.map[Dungeon.playerlocationy][Dungeon.playerlocationx] == "R":
            currentScreen = room
        if self.map[Dungeon.playerlocationy][Dungeon.playerlocationx] == "E":
            currentScreen = enemyroom
        if self.map[Dungeon.playerlocationy][Dungeon.playerlocationx] == "S":
            currentScreen = spawn

        self.findlocation()


    def moveup(self):
        global currentScreen

        print("You have moved up")
        self.playerlocationy -= 1

        if Dungeon.playerlocationy < 0:
            Dungeon.playerlocationy = 0
            print("No room there")

        if self.map[Dungeon.playerlocationy][Dungeon.playerlocationx] == "R":
            currentScreen = room
        if self.map[Dungeon.playerlocationy][Dungeon.playerlocationx] == "E":
            currentScreen = enemyroom
        if self.map[Dungeon.playerlocationy][Dungeon.playerlocationx] == "S":
            currentScreen = spawn

        self.findlocation()


    def movedown(self):
        global currentScreen

        print("You have moved down")
        self.playerlocationy += 1

        if Dungeon.playerlocationy > 4:
            Dungeon.playerlocationy = 4
            print("No room there")

        if self.map[Dungeon.playerlocationy][Dungeon.playerlocationx] == "R":
            currentScreen = room
        if self.map[Dungeon.playerlocationy][Dungeon.playerlocationx] == "E":
            currentScreen = enemyroom
        if self.map[Dungeon.playerlocationy][Dungeon.playerlocationx] == "S":
            currentScreen = spawn

        self.findlocation()


screen = display.set_mode((width, height))  # Sets size of screen
menuscreen = mainmenu()
instructionscreen = instructionmenu()

room = gamescreen(white)
enemyroom = enemyscreen(red)
spawn = spawnscreen(green)

currentScreen = menuscreen  # Creates object of the current screen

display.set_caption('MainMenu')
endProgram = False

Dungeon = dungeon()
Dungeon.generatemap()
Dungeon.display()

while not endProgram:  # pygame event loop
    for e in event.get():
        if e.type == QUIT:
            endProgram = True

        if e.type == MOUSEBUTTONDOWN:
            pos = mouse.get_pos()
            # print(pos)
            currentScreen.handleMouseInput(pos)

        if e.type == KEYDOWN:
            if e.key == K_RIGHT:
                Dungeon.moveright()

            if e.key == K_LEFT:
                Dungeon.moveleft()

            if e.key == K_UP:
                Dungeon.moveup()

            if e.key == K_DOWN:
                Dungeon.movedown()

    currentScreen.drawscreen(screen)
    display.update()

# bugs: phantom buttons
