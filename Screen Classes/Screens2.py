import pygame

pygame.init()

width = 1440
height = 900

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)


class abstractscreen():
    def __init__(self, colour):
        self.running = False
        self.colour = colour

    def fillscreen(self, screen):
        screen.fill(self.colour)


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
        self.buttonimg = pygame.transform.scale(self.buttonimg, (self.w, self.h))
        screen.blit(self.buttonimg, (self.x, self.y))

    def setCallback(self, callback):  # set a function and calls specific functions
        self.callback = callback

    def checkClick(self, pos):
        if self.rect.collidepoint(pos):
            self.callback()


class MainMenu():
    def __init__(self):
        # load buttons
        startbutton = pygame.image.load("startbutton.png")
        quitbutton = pygame.image.load("quitbutton.png")
        instructionbutton = pygame.image.load("howtoplaybutton.png")

        # button instances
        self.b1 = button(100, 700, 200, 100, startbutton)  # button (x,y,width,height,image)
        self.b2 = button(500, 500, 300, 105, quitbutton)  # button (x,y,width,height,image)
        # self.b2.action(self.quitgame)
        self.b3 = button(1000, 700, 250, 100, instructionbutton)  # button (x,y,width,height,image)

        # set up callbacks
        self.b2.setCallback(self.quitClicked)

        self.Buttons = [self.b1, self.b2, self.b3]

    def handleMouseInput(self, pos):
        for b in self.Buttons:
            b.checkClick(pos)

    def quitClicked(self):
        print("hhhhh")
        exit()

    def drawscreen(self, screen):
        self.backgroundimg = pygame.image.load("dungeonbg.jpg")
        self.backgroundimg = pygame.transform.scale(self.backgroundimg, (width, height))
        screen.blit(self.backgroundimg, (0, 0))
        self.b2.draw(screen)


screen = pygame.display.set_mode((width, height))  # Sets size of screen
pygame.display.set_caption("E")
menuScreen = MainMenu()

currentScreen = menuScreen  # Creates object of the current screen

endProgram = False

while not endProgram:  # pygame event loop

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            currentScreen.handleMouseInput(pos)
        if event.type == pygame.QUIT:
            endProgram = True
    currentScreen.drawscreen(screen)
    pygame.display.update()
pygame.quit()