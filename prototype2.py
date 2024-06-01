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

		self.b1 = button(100, 700, 200, 105, self.startbutton)  # button (x,y,width,height,image)

		self.b2 = button(550, 700, 215, 113, self.quitbutton)  # button (x,y,width,height,image)

		self.b3 = button(1000, 700, 250, 102, self.instructionbutton)  # button (x,y,width,height,image)

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
		Dungeon.generatemap()  # calls the generate map function
		Dungeon.display()  # calls the display function
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
		self.b1 = button(1200, 0, 200, 94, self.backbutton)  # button (x,y,width,height,image
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
		self.rlocked = False 
		self.dlocked = False
		self.llocked = False
		self.ulocked = False
	

	def drawscreen(self, screen):
		screen.fill(black) # colours the screen black
		self.topwall = draw.rect(screen, self.colour, Rect(0, 0, width, 20))  # drawing a rectangle (x,y,width,height)
		self.rightwall = draw.rect(screen, self.colour,Rect(width - 20, 0, 20, height))  # drawing a rectangle (x,y,width,height)
		self.leftwall = draw.rect(screen, self.colour, Rect(0, 0, 20, height))  # drawing a rectangle (x,y,width,height)
		self.bottomwall = draw.rect(screen, self.colour,Rect(0, height - 70, width, 20))  # drawing a rectangle (x,y,width,height), at school do height - 20 at home do height - 70

		door.drawdoor(screen) # draws all the doors


		player.draw(screen)  # Draws player to screen in game loop
		playershealthbar.draw(screen)  # Draws healthbar to screen
		for bullet in currentWeapon.bullets:  # For every bullet in the bullet list it:
			bullet.draw(screen)

		# This checks if the player reaches the end of any sides of the dungeon, if they do then it blocks off the door corresponding to that side (VALIDATION)
		if Dungeon.playerlocationy == 0:
			self.topwall = draw.rect(screen, self.colour, Rect(0, 0, width, 20))  # drawing a rectangle (x,y,width,height)
			self.ulocked = True
		else:
			self.ulocked = False
			#print("UTrue") 
		if Dungeon.playerlocationx == 4:
			self.rightwall = draw.rect(screen, self.colour,Rect(width - 20, 0, 20, height))  # drawing a rectangle (x,y,width,height)
			self.rlocked = True
		else:
			self.rlocked = False
			#print("RTrue")
		if Dungeon.playerlocationx == 0:
			self.leftwall = draw.rect(screen, self.colour,Rect(0, 0, 20, height))  # drawing a rectangle (x,y,width,height)
			self.llocked = True
		else:
			self.llocked = False
			#print("LTrue")
		if Dungeon.playerlocationy == 4:
			self.bottomwall = draw.rect(screen, self.colour, Rect(0, height - 70, width,20))  # drawing a rectangle (x,y,width,height), at school do height - 20 at home do height - 70
			self.dlocked = True
		else:
			self.dlocked = False
			#print("DTrue")

			#print("False")


class enemyscreen(gamescreen): # class enemyscreen - the next prototypes will add more to this screen
	pass

class spawnscreen(gamescreen): # class spawnscreen - the next prototypes will add more to this screen
	pass


class doors(): # class for the doors
	def __init__(self):
		self.topdoor = Rect((width / 2) - 100, 0, 200, 20)  # Top door hitbox
		self.rightdoor = Rect((width - 20), (height / 2) - 100, 20,200)  # right door hitbox
		self.leftdoor = Rect(0, (height / 2) - 100, 20, 200) # left door hitbox
		self.bottomdoor = Rect((width / 2) - 100, height - 70, 200,20)  # bottom door hitbox , at school do height - 20 at home do height - 70

	def drawdoor(self, screen): # function to draw the doors
		self.topdoor = draw.rect(screen, black,self.topdoor)  # drawing a rectangle (x,y,width,height)
		self.rightdoor = draw.rect(screen, black, self.rightdoor)  # drawing a rectangle (x,y,width,height)
		self.leftdoor = draw.rect(screen, black,self.leftdoor)  # drawing a rectangle (x,y,width,height)
		self.bottomdoor = draw.rect(screen, black,self.bottomdoor)  # drawing a rectangle (x,y,width,height), at school do height - 20 at home do height - 70

class button(): # the button class
	def __init__(self, x, y, w, h, image): # this sets up the button class to have the following attributes which can be entered (x co-ord, y co-ord, width, height, button image)
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.image = image
		self.rect = self.image.get_rect() # make the image into a rectangle
		print(self.image.get_rect())
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

		self.playerlocationx = self.spawnpointx
		self.playerlocationy = self.spawnpointy
		self.map[self.spawnpointy][self.spawnpointx] = "S" # after both loops are done it chooses a random index in the 2D array with the spawn point variables and sets it as 'S' which a spawn room
		self.spawnpointx = random.randint(0, 4)  # Chooses a random x co ordinate for the players spawn
		self.spawnpointy = random.randint(0, 4)  # Chooses a random y co ordinate for the players spawn
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
		if currentScreen.rlocked == False:
			player.x = 20
			player.y = 360
		if Dungeon.playerlocationx > 4: # boundary check - if the player meets the right side of the map they cannot go further VALIDATION
			Dungeon.playerlocationx = 4
			print("No room there")

		self.checkroom() # calls the function checkroom to the check the next room

	def moveleft(self): # the function to move left in the dungeon
		print("You have moved left")
		self.playerlocationx -= 1 # increments players x co-ord to move left in map
		if currentScreen.llocked == False:
			player.x = 1230
			player.y = 360

		if Dungeon.playerlocationx < 0: # boundary check - if the player meets the left side of the map they cannot go further VALIDATION
			Dungeon.playerlocationx = 0
			print("No room there")

		self.checkroom() # calls the function checkroom to the check the next room


	def moveup(self): # the function to move up in the dungeon
		print("You have moved up")
		self.playerlocationy -= 1 # increments players y co-ord to move up in map
		if currentScreen.ulocked == False:
			player.x = 640
			player.y = 660

		if Dungeon.playerlocationy < 0: # boundary check - if the player meets the top side of the map they cannot go further VALIDATION
			Dungeon.playerlocationy = 0
			print("No room there")

		self.checkroom() # calls the function checkroom to the check the next room


	def movedown(self): # the function to move down in the dungeon
		print("You have moved down")
		self.playerlocationy += 1 # increments players y co-ord to move down in map
		if currentScreen.dlocked == False:
			player.x = 640
			player.y = 20

		if Dungeon.playerlocationy > 4: # boundary check - if the player meets the bottom side of the map they cannot go further VALIDATION
			Dungeon.playerlocationy = 4
			print("No room there")

		self.checkroom() # calls the function checkroom to the check the next room

class player(): # class for the player
	def __init__(self, x, y, w, h): # constructor method for player for its x-position, y-position, width and height
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.velocity = 0 # Speed of the player, will be added to position to move player
		self.right = True # Starts the player facing right
		self.left = False
		self.up = False
		self.down = False
		self.no_dash_state = False # This is false so the player can dash when they spawn
		self.invincible = False # This is False so the player does not start of as being invincible
		self.dash_cooldown = 120 # The time to take for the player to be able to dash again (60fps)
		self.hit_cooldown = 60 # # The time to take for the player to be hit again (60FPS)


		self.playerRight = image.load("Player(Right).PNG") # Loads facing-right image of player
		self.playerRight = transform.scale(self.playerRight, (self.w, self.h)) # Scales facing-right image of player

		self.playerLeft = image.load("Player(Left).PNG") # Loads facing-left image of player
		self.playerLeft = transform.scale(self.playerLeft, (self.w, self.h)) # Scales facing-left image of player

		self.playerUp = image.load("Player(Up).PNG") # Loads facing-up image of player
		self.playerUp = transform.scale(self.playerUp, (self.w, self.h)) # Scales facing-up image of player

		self.playerDown = image.load("Player(Down).PNG") # Loads facing-down image of player
		self.playerDown = transform.scale(self.playerDown, (self.w, self.h)) # Scales facing-down image of player

	def draw(self, screen): # Function to draw player
		#draw.rect(screen,white,Rect(self.player_hitbox),1)
		if self.right: # If the player is facing right then it blits the facing-right image (VALIDATION)
			screen.blit(self.playerRight, (self.x, self.y))

		if self.left: # If the player is facing left then it blits the facing-left image (VALIDATION)
			screen.blit(self.playerLeft, (self.x, self.y))

		if self.down: # If the player is facing down then it blits the facing-down image (VALIDATION)
			screen.blit(self.playerDown, (self.x, self.y))

		if self.up: # If the player is facing up then it blits the facing-up image (VALIDATION)
			screen.blit(self.playerUp, (self.x, self.y))

	def update(self): # An update function that loops specific player functions in the game loop so it can be continuous whilst the game is running
		self.player_hitbox = Rect(self.x, self.y, self.w, self.h) # Creates a hitbox for the player for collisions


		if self.right: # if the player is facing right then it moves right whilst the key is pressed (VALIDATION)
			if self.x + 150 < width: # if the player is not touching the right border then it can move right whilst the key is pressed (VALIDATION)
				self.x = self.x + self.velocity

		if self.left:  # if the player is facing left then it moves left whilst the key is pressed (VALIDATION)
			if self.x > 0:  # if the player is not touching the left border then it can move left whilst the key is pressed (VALIDATION)
				self.x = self.x - self.velocity

		if self.down: # if the player is not touching the botton border then it can move down whilst the key is pressed (VALIDATION)
			if self.y + 158 < height: # if the player is not touching the bottom border then it can move down whilst the key is pressed (VALIDATION)
				self.y = self.y + self.velocity

		if self.up: # if the player is not touching the top border then it can move up whilst the key is pressed (VALIDATION)
			if self.y > 0: # if the player is not touching the top border then it can move up whilst the key is pressed (VALIDATION)
				self.y = self.y - self.velocity

		if self.no_dash_state == True: # If this is True the player cannot dash again until the timer is up (VALIDATION)
			if self.dash_cooldown >= 0: # If this is greater than 0 then it decreases from its given value to 0 (VALIDATION)
				self.dash_cooldown = self.dash_cooldown - 1
				print(self.dash_cooldown)
				if self.dash_cooldown == 0: # If this value becomes 0 then the player can dash again
					self.no_dash_state = False

		if self.invincible == True: # If this is True the player cannot get hit again until the timer is up (VALIDATION)
			if self.hit_cooldown >= 0: # If this is greater than 0 then it decreases from its given value to 0 (VALIDATION)
				self.hit_cooldown = self.hit_cooldown - 1
				print(self.hit_cooldown)
				if self.hit_cooldown == 0: # If this value becomes 0 then the player can get hit again
					self.invincible = False
		if currentScreen == spawn:  # While the player is in the spawn room, they heal (VALIDATION)
			player.heal(10)

		if self.player_hitbox.colliderect(door.topdoor): # VALIDATION collision detection with top door
			Dungeon.moveup()
		if self.player_hitbox.colliderect(door.rightdoor): # VALIDATION collision detection with right door
			Dungeon.moveright()
		if self.player_hitbox.colliderect(door.bottomdoor): # VALIDATION collision detection with bottom door
			Dungeon.movedown()
		if self.player_hitbox.colliderect(door.leftdoor): # VALIDATION collision detection with left door
			Dungeon.moveleft()


	def moveright(self): # The function to move the player right
		self.right = True # right becomes True as the player is facing right
		self.left = False
		self.down = False
		self.up = False
		self.velocity = 3 # The speed the player is given

	def moveleft(self): # The function to move the player left
		self.right = False
		self.left = True # left becomes True as the player is facing left
		self.down = False
		self.up = False
		self.velocity = 3 # The speed the player is given

	def movedown(self): # The function to move the player down
		self.right = False
		self.left = False
		self.down = True # down becomes True as the player is facing down
		self.up = False
		self.velocity = 3 # The speed the player is given

	def moveup(self): # The function to move the player up
		self.right = False
		self.left = False
		self.down = False
		self.up = True # up becomes True as the player is facing up
		self.velocity = 3 # The speed the player is given

	def dash(self): # The function to allow the player to dash
		if self.no_dash_state == False: # If this is false then the player can dash in any direction (VALIDATION)

			if self.right: # if the player is facing right thne it dashes right (VALIDATION)
				if self.x + 192 < width: # if the player is not touching the right border then it can dash (VALIDATION)
					self.x = self.x + 80 # Adds a certain amount of extra distance to the players current distance
					self.no_dash_state = True # This value is set to true and thr playe cannot dash until the cooldown is over

			if self.left: # if the player is facing left thne it dashes left (VALIDATION)
				if self.x > 0: # if the player is not touching the left border then it can dash (VALIDATION)
					self.x = self.x - 80 # Adds a certain amount of extra distance to the players current distance
					self.no_dash_state = True # This value is set to true and thr playe cannot dash until the cooldown is over

			if self.down: # if the player is facing down thne it dashes down (VALIDATION)
				if self.y + 202 < height: # if the player is not touching the bottom border then it can dash (VALIDATION)
					self.y = self.y + 80 # Adds a certain amount of extra distance to the players current distance
					self.no_dash_state = True # This value is set to true and thr playe cannot dash until the cooldown is over

			if self.up: # if the player is facing up thne it dashes up (VALIDATION)
				if self.y > 0: # if the player is not touching the top border then it can dash (VALIDATION)
					self.y = self.y - 80 # Adds a certain amount of extra distance to the players current distance
					self.no_dash_state = True # This value is set to true and thr playe cannot dash until the cooldown is over

			self.dash_cooldown = 120 # After the player dashes in any direction then it resets the dash cooldown

	def hit(self, damage): # This function damages the player and takes in the damage as a parameter
			print(self.hit_cooldown)
			if self.invincible == False: # if this value is false then the player can be damaged (VALIDATION)
				playershealthbar.health = playershealthbar.health - damage # Subtracts players health with damage value
				self.invincible = True # After the player has been hit this is set to True and the playe cannot be hit until the cooldown ends
				print(playershealthbar.health)
				if playershealthbar.health <= 0: # A check to see if the players health hits 0 or less so then a game over can be initiated (VALIDATION)
					instructionscreen.backtomain() # Sends user back to main menu
					player.x = 630 # resets players x co-ordinate
					player.y = 340 # resets players y co-ordinate
				self.hit_cooldown = 60 # after the player gets hit then it resets the invincibilty cooldown

	def heal(self, heal): # This function heal and restores the players health and takes in tehheal value as a parameter
		playershealthbar.health = playershealthbar.health + heal # Adds together the players health and heal value
		#print(playershealthbar.health)
		if playershealthbar.health >= 200: # A check to see if the player goes over its max health,
			#print("Health full")
			playershealthbar.health = 200 # Makes sure the players health doesnt go over its max health


class projectile(): # A class for the projectiles that are shot
	def __init__(self, x, y, w, h, direction): # Constructor method that has the x-co-ordinate, y-co-ordinate, width and height and direction of the projectile
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.direction = direction

	def draw(self, screen): # function to draw the projectile
		draw.rect(screen, white, Rect(self.x, self.y, self.w, self.h))

	def update(self): # An update function to allow the projectile to move across the screen
		for bullet in currentWeapon.bullets: # Checks every bullet in the bullet list in the weapons class
			if self.direction == 1:  # Checks if the direction value = 1 (VALIDATION)
				if self.x < width: # Checks if the projectile has hit the right border (VALIDATION)
					self.x = self.x + currentWeapon.velocity # Moves the bullet right
				else:
					currentWeapon.bullets.pop(currentWeapon.bullets.index(bullet)) # When the bullet hits a border it gets destroyed

			if self.direction == 2: # Checks if the direction value = 2 (VALIDATION)
				if self.x > 0: # Checks if the projectile has hit the left border (VALIDATION)
					self.x = self.x - currentWeapon.velocity # Moves the bullet left
				else:
					currentWeapon.bullets.pop(currentWeapon.bullets.index(bullet)) # When the bullet hits a border it gets destroyed

			if self.direction == 3: # Checks if the direction value = 3 (VALIDATION)
				if self.y > 0: # Checks if the projectile has hit the top border (VALIDATION)
					self.y = self.y - currentWeapon.velocity # Moves the bullet up
				else:
					currentWeapon.bullets.pop(currentWeapon.bullets.index(bullet)) # When the bullet hits a border it gets destroyed

			if self.direction == 4: # Checks if the direction value = 4 (VALIDATION)
				if self.y < height: # Checks if the projectile has hit the bottom border (VALIDATION)
					self.y = self.y + currentWeapon.velocity # Moves the bullet down
				else:
					currentWeapon.bullets.pop(currentWeapon.bullets.index(bullet)) # When the bullet hits a border it gets destroyed


class weapon(): # The class for the weapon will store the projectiles used aswell
	def __init__(self, damage, velocity, bulletcount): # Constructor method which stores damage, velocity and bulletcount of the weapon
		self.damage = damage
		self.bulletcount = bulletcount # This attribute gives how many bullets can be on screen
		self.bullets = [] # The bullet list which stores all bullets shot by the player
		self.velocity = velocity

	def fire(self): # This function fires the bullets and changes their direction
		if player.right: # If the player is facing right the projectile direction value is set to 1 (VALIDATION)
			projectile.direction = 1

		if player.left: # If the player is facing left the projectile direction value is set to 2 (VALIDATION)
			projectile.direction = 2

		if player.up: # If the player is facing up the projectile direction value is set to 3 (VALIDATION)
			projectile.direction = 3

		if player.down: # If the player is facing down the projectile direction value is set to 4 (VALIDATION)
			projectile.direction = 4

		bullet = projectile(round(player.x + player.w // 2), round(player.y + player.h // 2), 10, 10,projectile.direction) # Instantiates an object of the projectile class called bullet - (x,y,width,height,direction)
		if len(self.bullets) < self.bulletcount: # checks if the amount of bullets in the list is less than the bullet count
			self.bullets.append(bullet) # If the list is smaller than the bullet count then it appends a bullet into the array which is released on screen in the given direction

class healthbar(): # Class for the health bar
	def __init__(self,health,x,y,w,h): # constructor method which stores the health value, x-coordinate, y-coordinate, width and height of the healthbar
		self.health = health
		self.x = x
		self.y = y
		self.w = w
		self.h = h

	def draw(self,screen): # function to draw the health bar on screen
		draw.rect(screen,red,Rect(self.x,self.y,self.w,self.h)) # Creates a red rectangle which shows if the health bar is being depleted or is depleted
		draw.rect(screen,healthbar_green,Rect(self.x,self.y,self.w - (1 *(200 - self.health)),self.h)) # Draws a green rectangle that has its width reduced depending on current players health



screen = display.set_mode((width, height))  # Sets size of screen
menuscreen = mainmenu() # creates instance of an object for the mainmenu class
instructionscreen = instructionmenu() # creates instance of an object for the instructionmenu class

room = gamescreen(white) # creates instance of an object for the gamescreen class and gives it the colour white
enemyroom = enemyscreen(red) # creates instance of an object for the enemyscreen class and gives it the colour red
spawn = spawnscreen(green) # creates instance of an object for the spawnscreen class and gives it the colour green
door = doors()  # creates an instance of an object for the class 'doors'

player = player(630, 340, 128, 136)  # Instatiates an object for the player class called player - (x,y,width,height)
pistol = weapon(10, 20, 1) # Instatiates an object for the weapon class called pistol - (damage,velocity,damage)
currentWeapon = pistol # Creates a variable which sets the current weapon to be the pistol (can change if new weapons are introduced)
playershealthbar = healthbar(200,30,30,200,20) # # Instatiates an object for the healthbar class called playershealthbar - (health,x,y,width,height)

currentScreen = menuscreen  # Sets the current screen to start off with the main menu

display.set_caption('Dungeon Crawler')
endProgram = False

Dungeon = dungeon() # creates instance of an object for the dungeon class


while not endProgram:  # pygame event loop
	for e in event.get():
		if e.type == QUIT:
			endProgram = True

		if e.type == MOUSEBUTTONDOWN:
			pos = mouse.get_pos() # gets the position of the mouse
			print(pos)
			currentScreen.handleMouseInput(pos) # calls the handleMouseInput function and make it pass through the position of the mouse when it is clicked

		# I have set arrow keys to help navigate throught the dungeon, this is for testing purposes only, in prototype 2 this will change to the player colliding with doors to navigate
		if e.type == KEYDOWN: # VALIDATION
			if e.key == K_d:  # Moves player right is 'd' key is pressed
				player.moveright()


			if e.key == K_a:  # Moves player left if 'a' key is pressed
				player.moveleft()


			if e.key == K_s:  # Moves player down if 's' key is pressed
				player.movedown()


			if e.key == K_w:  # Moves player up if 'w' key is pressed
				player.moveup()


			if e.key == K_RSHIFT or e.key == K_LSHIFT:  # Player dashes if either shift key is pressed
				player.dash()

			if e.key == K_SPACE:  # Player shoots if space bar is pressed
				pistol.fire()

			if e.key == K_g:  # Player loses health if 'g' key is pressed - only for testing
				player.hit(50)

			if e.key == K_h:  # Player gains health if 'h' key is pressed - only for testing
				player.heal(10)

		if e.type == KEYUP:  # If any movement key is released then the player stops moving VALIDATION
			if e.key == K_d and player.right:
				player.velocity = 0
			if e.key == K_a and player.left:
				player.velocity = 0
			if e.key == K_w and player.up:
				player.velocity = 0
			if e.key == K_s and player.down:
				player.velocity = 0

	currentScreen.drawscreen(screen) # draws current screen
	player.update() # Updates player in game loop
	for bullet in currentWeapon.bullets: # For every bullet in the bullet list it:
		bullet.update() # Updates the bullet
	display.update() # updates screen



