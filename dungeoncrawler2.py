# This one contains all the bugs
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


class abstractscreen(): # creates the screen class which is a parent class for the other screens
    def __init__(self):
        pass

    def handleMouseInput(self, pos): # A function that handles the mouse inputs (e.g. clicking)
        for b in self.listOfButtons:
            b.checkClick(pos) # calls the checkClick function for every button on screen


class mainmenu(abstractscreen): # main menu class

    def __init__(self):
        self.startbutton = image.load("startbutton.PNG") # loads image of the start button
        self.quitbutton = image.load("quitbutton.PNG") # loads image of the quit button
        self.instructionbutton = image.load("howtoplaybutton.PNG") # loads image of the how to play button

        self.b1 = button(100, 700, 200, 100, self.startbutton)  # button (x,y,width,height,image)

        self.b2 = button(500, 700, 300, 105, self.quitbutton)  # button (x,y,width,height,image)

        self.b3 = button(1000, 700, 250, 100, self.instructionbutton)  # button (x,y,width,height,image)

        self.b1.setCallback(self.loadgame) # Assigns the function 'loadgame' to the start button
        self.b2.setCallback(self.quitgame) # Assigns the function 'quitgame' to the quit button
        self.b3.setCallback(self.viewinstructions) # Assigns the function 'viewinstructions' to the instruction button

        self.listOfButtons = [self.b1, self.b2, self.b3] # All the buttons for the main menu are stored in an array

    def drawscreen(self, screen): # The function to draw the screen
        self.backgroundimg = image.load("dungeonbg.jpg") # loads background image
        self.backgroundimg = transform.scale(self.backgroundimg, (width, height)) # transforms background image
        screen.blit(self.backgroundimg, (0, 0)) # blits background on to screen

        for b in self.listOfButtons:
            b.draw(screen) # draws every single button in the array for the main menu

    def loadgame(self): # the function to load the game
        global currentScreen
        currentScreen = spawn # the current screen is switched to the spawnscreen

        print("Game Loaded")

    def quitgame(self): # the function to quit the game
        print("Game over")
        exit()

    def viewinstructions(self): # the function to view instructions
        global currentScreen
        currentScreen = instructionscreen # the current screen is switched to the instruction screen


class instructionmenu(abstractscreen): # instruction menu class
    def __init__(self):
        self.backbutton = image.load("backbutton.PNG") # loads image for the back button
        self.b1 = button(1200, 0, 200, 100, self.backbutton)  # button (x,y,width,height,image
        self.b1.setCallback(self.backtomain) # sets the 'backtomain' function the back button
        self.listOfButtons = [self.b1] # the back button is stored in the array

    def drawscreen(self, screen): # the function to draw the instruction screen
        self.instructions = image.load("instructions.png") # loads the image for the instructions
        self.instructions = transform.scale(self.instructions, (width, height)) # # scales the instruction button
        screen.fill(black) # colours the screen black
        screen.blit(self.instructions, (0, 0)) # blits the instruction on to the screen

        for b in self.listOfButtons:
            b.draw(screen) # draws the buttons in the array (back button)

    def backtomain(self): # the function to go back to the main menu
        global currentScreen
        currentScreen = menuscreen # switches the current screen to the main menu
        print("Menu loaded")


class gamescreen(abstractscreen): # the gamescreen class
    def __init__(self, colour): # sets up the gamescreen class and allows you to enter a colour for the walls
        self.listOfButtons = [] # an empty button array for any future buttons to be used on this screen
        self.colour = colour

    def drawscreen(self, screen):
        screen.fill(black) # colours the screen black
        self.topwall = draw.rect(screen, self.colour, Rect(0, 0, width, 20))  # drawing a rectangle (x,y,width,height)
        self.rightwall = draw.rect(screen, self.colour,Rect(width - 20, 0, 20, height))  # drawing a rectangle (x,y,width,height)
        self.leftwall = draw.rect(screen, self.colour, Rect(0, 0, 20, height))  # drawing a rectangle (x,y,width,height)
        self.bottomwall = draw.rect(screen, self.colour,Rect(0, height - 70, width, 20))  # drawing a rectangle (x,y,width,height), at school do height - 20 at home do height - 70





        self.door = doors() # creates an instance of an object for the class 'doors'
        self.door.drawdoor(screen) # draws all the doors

        # This checks if the player reaches the end of any sides of the dungeon, if they do then it blocks off the door corresponding to that side (VALIDATION)
        if Dungeon.playerlocationy == 0:
            self.topwall = draw.rect(screen, self.colour, Rect(0, 0, width, 20))  # drawing a rectangle (x,y,width,height)
        if Dungeon.playerlocationx == 4:
            self.rightwall = draw.rect(screen, self.colour,Rect(width - 20, 0, 20, height))  # drawing a rectangle (x,y,width,height)
        if Dungeon.playerlocationx == 0:
            self.leftwall = draw.rect(screen, self.colour,Rect(0, 0, 20, height))  # drawing a rectangle (x,y,width,height)
        if Dungeon.playerlocationy == 4:
            self.bottomwall = draw.rect(screen, self.colour, Rect(0, height - 70, width,20))  # drawing a rectangle (x,y,width,height), at school do height - 20 at home do height - 70


class enemyscreen(gamescreen): # class enemyscreen - the next prototypes will add more to this screen
    pass

class spawnscreen(gamescreen): # class spawnscreen - the next prototypes will add more to this screen
    pass


class doors(): # class for the doors
    def __init__(self):
        pass

    def drawdoor(self, screen): # function to draw the doors
        self.topdoor = draw.rect(screen, black,Rect((width / 2) - 100, 0, 200, 20))  # drawing a rectangle (x,y,width,height)
        self.rightdoor = draw.rect(screen, black, Rect(width - 20, (height / 2) - 100, 20,200))  # drawing a rectangle (x,y,width,height)
        self.leftdoor = draw.rect(screen, black,Rect(0, (height / 2) - 100, 20, 200))  # drawing a rectangle (x,y,width,height)
        self.bottomdoor = draw.rect(screen, black, Rect((width / 2) - 100, height - 70, 200,20))  # drawing a rectangle (x,y,width,height), at school do height - 20 at home do height - 70

class button(): # the button class
    def __init__(self, x, y, w, h, image): # this sets up the button class to have the following attributes which can be entered (x co-ord, y co-ord, width, height, button image)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = image
        self.rect = self.image.get_rect() # make the image into a rectangle
        self.rect.topleft = (x, y) # positions the rectangle

    def draw(self, screen): # function to draw the button
        self.buttonimg = self.image
        self.buttonimg = transform.scale(self.buttonimg, (self.w, self.h)) # scales the image for button
        screen.blit(self.buttonimg, (self.x, self.y)) # blits the button on to the screen with the x and y co-ords

    def setCallback(self, callback): # the function to set actions to the buttons
        self.callback = callback

    def checkClick(self, pos): # the function to check the click inputs on the buttons
        if self.rect.collidepoint(pos):
            self.callback() # if the button collides with the position of the mouse on click then it calls the action of button (VALIDATION)


class dungeon(): # the dungeon class
    def __init__(self):
        self.map = [[0, 0, 0, 0, 0], # the dungeon itself is a 2D array, it is smaller for now for testing purposes but will 10x10 for the final prototype
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]]

        self.spawnpointx = random.randint(0, 4) # Chooses a random x co ordinate for the players spawn
        self.spawnpointy = random.randint(0, 4) # Chooses a random y co ordinate for the players spawn
        self.playerlocationx = self.spawnpointx
        self.playerlocationy = self.spawnpointy
        self.enemy_room = random.randint(1, 2) # Chooses a random number to give a 50% chance for a room to be an enemy room

    def generatemap(self): # the function to generate the map
        posx = 0
        posy = 0
        while posx < 5 and posy < 5: # a while loop to iterate over the 2D array
            self.map[posx][posy] = "R" # sets every index to be 'R' which is a normal room
            posx = posx + 1 # increments posx to move to next column
            while posx == 5:
                posx = 0
                posy = posy + 1 # increments posy to move to next row

        posx = 0
        posy = 0

        while posx < 5 and posy < 5: # Another while loop to iterate over the 2D array again to add enemy rooms
            if self.enemy_room == 2: # Checks if enemy room = 2 which is a 50% chance (VALIDATION)
                self.map[posx][posy] = "E" # if enemy room = 2 then that index is set to 'E' which is an enemy room
            self.enemy_room = random.randint(1, 2) # Randomises the variable again
            posx = posx + 1 # increments posx to move to next column
            while posx == 5:
                posx = 0
                posy = posy + 1 # increments posy to move to next row

        self.map[self.spawnpointy][self.spawnpointx] = "S" # after both loops are done it chooses a random index in the 2D array with the spawn point variables and sets it as 'S' which a spawn room

        if Dungeon.playerlocationx > 4: # boundary check - if the player meets the right side of the map they cannot go further VALIDATION
            Dungeon.playerlocationx = 4
            print("No room there")

        if Dungeon.playerlocationx < 0: # boundary check - if the player meets the left side of the map they cannot go further VALIDATION
            Dungeon.playerlocationx = 0
            print("No room there")


        if Dungeon.playerlocationy < 0: # boundary check - if the player meets the top side of the map they cannot go further VALIDATION
            Dungeon.playerlocationy = 0
            print("No room there")

        if Dungeon.playerlocationy > 4: # boundary check - if the player meets the bottom side of the map they cannot go further VALIDATION
            Dungeon.playerlocationy = 4
            print("No room there")

        return self.map # returns the map after it has been generated

    def display(self): # this function displays the 2D array in the terminal
        i = 0
        while i < len(self.map):
            print(self.map[i])
            i += 1

    def findlocation(self): # this function returns the location of the player in the dungeon
        print("You are in the coordinates:", "(", self.playerlocationx, ",", self.playerlocationy, ")", "Your are in:",
              self.map[self.playerlocationy][self.playerlocationx])

        self.display()
        print("")

    def checkroom(self): # a function to check the adjacent rooms
        global currentScreen

        # VALIDATION
        if self.map[Dungeon.playerlocationy][Dungeon.playerlocationx] == "R": # if next position has the index 'R" then current screen is switched to a normal room
            currentScreen = room
        if self.map[Dungeon.playerlocationy][Dungeon.playerlocationx] == "E": # if next position has the index 'E" then current screen is switched to an enemy room
            currentScreen = enemyroom
        if self.map[Dungeon.playerlocationy][Dungeon.playerlocationx] == "S": # if next position has the index 'S" then current screen is switched to the spawn room
            currentScreen = spawn

        self.findlocation() # calls the findlocation function, it returns the position of the player

    def moveright(self): # the function to move right in the dungeon

        print("You have moved right")
        self.playerlocationx += 1 # increments players x co-ord to move right in map
        self.checkroom() # calls the function checkroom to the check the next room

    def moveleft(self): # the function to move left in the dungeon
        print("You have moved left")
        self.playerlocationx -= 1 # increments players x co-ord to move left in map
        self.checkroom() # calls the function checkroom to the check the next room


    def moveup(self): # the function to move up in the dungeon
        print("You have moved up")
        self.playerlocationy -= 1 # increments players y co-ord to move up in map
        self.checkroom() # calls the function checkroom to the check the next room


    def movedown(self): # the function to move down in the dungeon
        print("You have moved down")
        self.playerlocationy += 1 # increments players y co-ord to move down in map
        self.checkroom() # calls the function checkroom to the check the next room


screen = display.set_mode((width, height))  # Sets size of screen
menuscreen = mainmenu() # creates instance of an object for the mainmenu class
instructionscreen = instructionmenu() # creates instance of an object for the instructionmenu class

room = gamescreen(white) # creates instance of an object for the gamescreen class and gives it the colour white
enemyroom = enemyscreen(red) # creates instance of an object for the enemyscreen class and gives it the colour red
spawn = spawnscreen(green) # creates instance of an object for the spawnscreen class and gives it the colour green

currentScreen = menuscreen  # Sets the current screen to start off with the main menu

display.set_caption('Dungeon Crawler')
endProgram = False

Dungeon = dungeon() # creates instance of an object for the dungeon class
Dungeon.generatemap() # calls the generate map function
Dungeon.display() # calls the display function

while not endProgram:  # pygame event loop
    for e in event.get():
        if e.type == QUIT:
            endProgram = True

        if e.type == MOUSEBUTTONDOWN: # VALIDATION
            pos = mouse.get_pos() # gets the position of the mouse
            # print(pos)
            currentScreen.handleMouseInput(pos) # calls the handleMouseInput function and make it pass through the position of the mouse when it is clicked

        # I have set arrow keys to help navigate throught the dungeon, this is for testing purposes only, in prototype 2 this will change to the player colliding with doors to navigate
        if e.type == KEYDOWN: # VALIDATION
            if e.key == K_RIGHT:
                Dungeon.moveright()

            if e.key == K_LEFT:
                Dungeon.moveleft()

            if e.key == K_UP:
                Dungeon.moveup()

            if e.key == K_DOWN:
                Dungeon.movedown()

    currentScreen.drawscreen(screen) # draws current screen
    display.update() # updates screen

# bug 1: phantom buttons, map index turns negative and loops across array, border validation not working - game crashes when you go off border
# bug 2: map index turns negative and loops across array
# bug 3: border validation not working - game crashes when you go off border

#bug 2 and 3 have the same fix