from pygame import *

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
        self.running = False
        self.nextscreen = self

    def getNextScreen(self):
        return self.nextscreen

    def handleMouseInput(self, pos):
        for b in self.listOfButtons:
            b.checkClick(pos)

class gamescreen(abstractscreen):
    def __init__(self):
        self.nextscreen = self
        self.listOfButtons = []

    def drawscreen(self,screen):
        screen.fill(black)
        self.topwall = draw.rect(screen, white, Rect(0, 0, width, 20))  # drawing a rectangle (x,y,width,height)
        self.rightwall = draw.rect(screen, white, Rect(width-20, 0, 20, height))  # drawing a rectangle (x,y,width,height)
        self.leftwall = draw.rect(screen, white, Rect(0, 0, 20, height))  # drawing a rectangle (x,y,width,height)
        self.bottomwall = draw.rect(screen, white, Rect(0, height-70, width, 20))  # drawing a rgleectan (x,y,width,height)

        self.door = doors()
        self.door.drawdoor(screen)

class doors():
    def __init__(self):
        pass

    def drawdoor(self,screen):
        self.topdoor = draw.rect(screen, black, Rect((width/2) - 100, 0, 200, 20))  # drawing a rectangle (x,y,width,height)
        self.rightdoor = draw.rect(screen, black, Rect(width-20,(height/2) - 100 , 20, 200))  # drawing a rectangle (x,y,width,height)
        self.leftdoor = draw.rect(screen, black, Rect(0, (height/2) - 100 , 20, 200))  # drawing a rectangle (x,y,width,height)
        self.bottomdoor = draw.rect(screen, black, Rect((width/2) - 100, height-70, 200, 20))  # drawing a rectangle (x,y,width,height)

screen = display.set_mode((width, height))  # Sets size of screen
gamescreen = gamescreen()


currentScreen = gamescreen  # Creates object of the current screen

display.set_caption('gamescreen')
endProgram = False

while not endProgram:  # pygame event loop
    for e in event.get():
        if e.type == QUIT:
            endProgram = True

        if e.type == MOUSEBUTTONDOWN:
            pos = mouse.get_pos()
            currentScreen.handleMouseInput(pos)


    currentScreen.drawscreen(screen)
    currentScreen.getNextScreen()
    display.update()

