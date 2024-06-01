from pygame import *

init()
import random

class dungeon():
    def __init__(self):
        self.map = [[0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0]]


        self.spawnpointx = random.randint(0,2)
        self.spawnpointy = random.randint(0, 2)
        self.playerlocationx = self.spawnpointx
        self.playerlocationy = self.spawnpointy
        self.enemy_room = random.randint(1,2)



    def generatemap(self):
        posx = 0
        posy = 0
        while posx < 10 and posy < 10:
            self.map[posx][posy] = "E"
            posx = posx + 1
            while posx == 10:
                posx = 0
                posy = posy + 1

        posx = 0
        posy = 0

        while posx < 10 and posy < 10:
            if self.enemy_room == 2:
                self.map[posx][posy] = "R"
            self.enemy_room = random.randint(1, 2)
            posx = posx + 1
            while posx == 10:
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
        if Dungeon.playerlocationx < 0:
            Dungeon.playerlocationx = 0
            print("No room there")
        if Dungeon.playerlocationx > 9:
            Dungeon.playerlocationx = 9
            print("No room there")

        if Dungeon.playerlocationy < 0:
            Dungeon.playerlocationy = 0
            print("No room there")

        if Dungeon.playerlocationy > 9:
            Dungeon.playerlocationy = 9
            print("No room there")

        print("You are in the coordinates:","(",self.playerlocationx,",",self.playerlocationy,")","Your are in:",self.map[self.playerlocationy][self.playerlocationx])

        self.display()
        print("")



    def moveright(self):
        print("You have moved right")
        self.playerlocationx += 1
        self.findlocation()


    def moveleft(self):
        print("You have moved left")
        self.playerlocationx -= 1
        self.findlocation()

    def moveup(self):
        print("You have moved up")
        self.playerlocationy -= 1
        self.findlocation()

    def movedown(self):
        print("You have moved down")
        self.playerlocationy += 1
        self.findlocation()




Dungeon = dungeon()
print("Note - the starting indexes is 0")

Dungeon.generatemap()
Dungeon.display()
while True:

    for e in event.get():
        if e.type == constants.QUIT: # to quit game (close tab)
            pass



        if e.type == KEYDOWN:

            if e.key == K_RIGHT:
                Dungeon.moveright()

            if e.key == K_LEFT:
                Dungeon.moveleft()

            if e.key == K_UP:
                Dungeon.moveup()

            if e.key == K_DOWN:
                Dungeon.movedown()

