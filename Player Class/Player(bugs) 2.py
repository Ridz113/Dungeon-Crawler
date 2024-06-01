from pygame import *



init()

width = 1440
height = 900

red = (255, 0, 0)
green = (0, 255, 0)
healthbar_green = (42,234,46) # Green for the healthbar
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)


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
        if self.right: # If the player is facing right then it blits the facing-right image (VALIDATION)
            screen.blit(self.playerRight, (self.x, self.y))

        if self.left: # If the player is facing left then it blits the facing-left image (VALIDATION)
            screen.blit(self.playerLeft, (self.x, self.y))

        if self.down: # If the player is facing down then it blits the facing-down image (VALIDATION)
            screen.blit(self.playerDown, (self.x, self.y))

        if self.up: # If the player is facing up then it blits the facing-up image (VALIDATION)
            screen.blit(self.playerUp, (self.x, self.y))

    def update(self): # An update function that loops specific player functions in the game loop so it can be continuous whilst the game is running
        if self.right: # if the player is facing right then it moves right whilst the key is pressed (VALIDATION)
            if self.x + 192 < width: # if the player is not touching the right border then it can move right whilst the key is pressed (VALIDATION)
                self.x = self.x + self.velocity

        if self.left:  # if the player is facing left then it moves left whilst the key is pressed (VALIDATION)
            if self.x > 0:  # if the player is not touching the left border then it can move left whilst the key is pressed (VALIDATION)
                self.x = self.x - self.velocity

        if self.down: # if the player is not touching the botton border then it can move down whilst the key is pressed (VALIDATION)
            if self.y + 202 < height: # if the player is not touching the bottom border then it can move down whilst the key is pressed (VALIDATION)
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

    def moveright(self): # The function to move the player right
        self.right = True # right becomes True as the player is facing right
        self.left = False
        self.down = False
        self.up = False
        self.velocity = 10 # The speed the player is given

    def moveleft(self): # The function to move the player left
        self.right = False
        self.left = True # left becomes True as the player is facing left
        self.down = False
        self.up = False
        self.velocity = 10 # The speed the player is given

    def movedown(self): # The function to move the player down
        self.right = False
        self.left = False
        self.down = True # down becomes True as the player is facing down
        self.up = False
        self.velocity = 10 # The speed the player is given

    def moveup(self): # The function to move the player up
        self.right = False
        self.left = False
        self.down = False
        self.up = True # up becomes True as the player is facing up
        self.velocity = 10 # The speed the player is given

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
                    print("Game Over - Back to main menu")
                self.hit_cooldown = 60 # after the player gets hit then it resets the invincibilty cooldown

    def heal(self, heal): # This function heal and restores the players health and takes in tehheal value as a parameter
        playershealthbar.health = playershealthbar.health + heal # Adds together the players health and heal value
        print(playershealthbar.health)
        if playershealthbar.health >= 200: # A check to see if the player goes over its max health,
            print("Health full")
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

        for bullet in currentWeapon.bullets: # Checks every bullet in the bullet list in the weapons class
            if projectile.direction == 1:  # Checks if the direction value = 1 (VALIDATION)
                if bullet.x < width: # Checks if the projectile has hit the right border (VALIDATION)
                    bullet.x = bullet.x + currentWeapon.velocity # Moves the bullet right
                else:
                    currentWeapon.bullets.pop(currentWeapon.bullets.index(bullet)) # When the bullet hits a border it gets destroyed

            if bullet.direction == 2: # Checks if the direction value = 2 (VALIDATION)
                if bullet.x > 0: # Checks if the projectile has hit the left border (VALIDATION)
                    bullet.x = bullet.x - currentWeapon.velocity # Moves the bullet left
                else:
                    currentWeapon.bullets.pop(currentWeapon.bullets.index(bullet)) # When the bullet hits a border it gets destroyed

            if projectile.direction == 3: # Checks if the direction value = 3 (VALIDATION)
                if bullet.y > 0: # Checks if the projectile has hit the top border (VALIDATION)
                    bullet.y = bullet.y - currentWeapon.velocity # Moves the bullet up
                else:
                    currentWeapon.bullets.pop(currentWeapon.bullets.index(bullet)) # When the bullet hits a border it gets destroyed

            if projectile.direction == 4: # Checks if the direction value = 4 (VALIDATION)
                if bullet.y < height: # Checks if the projectile has hit the bottom border (VALIDATION)
                    bullet.y = bullet.y + currentWeapon.velocity # Moves the bullet down
                else:
                    currentWeapon.bullets.pop(currentWeapon.bullets.index(bullet)) # When the bullet hits a border it gets destroyed

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



screen = display.set_mode((width, height))
player = player(100, 100, 192, 202) # Instatiates an object for the player class called player -
pistol = weapon(10, 50, 1) # Instatiates an object for the weapon class called pistol - (damage,velocity,damage)
currentWeapon = pistol # Creates a variable which sets the current weapon to be the pistol (can change if new weapons are introduced)
playershealthbar = healthbar(200,30,30,200,20) # # Instatiates an object for the healthbar class called playershealthbar - (health,x,y,width,height)
display.set_caption('Player')
endProgram = False
clock = time.Clock() # Creates a clock using the time library to set FPS

while not endProgram:  # pygame event loop

    clock.tick(60) # Sets FPS to be 60

    for e in event.get():
        if e.type == QUIT:
            endProgram = True

        if e.type == KEYDOWN:
            if e.key == K_d: # Moves player right is 'd' key is pressed
                player.moveright()

            if e.key == K_a: # Moves player left if 'a' key is pressed
                player.moveleft()

            if e.key == K_s: # Moves player down if 's' key is pressed
                player.movedown()

            if e.key == K_w: # Moves player up if 'w' key is pressed
                player.moveup()

            if e.key == K_RSHIFT or e.key == K_LSHIFT: # Player dashes if either shift key is pressed
                player.dash()

            if e.key == K_SPACE: # Player shoots if space bar is pressed
                pistol.fire()

            if e.key == K_g: # Player loses health if 'g' key is pressed - only for testing
                player.hit(10)

            if e.key == K_h: # Player gains health if 'h' key is pressed - only for testing
                player.heal(10)

        if e.type == KEYUP: # If any movement key is released then the player stops moving
            if e.key == K_d and player.right:
                player.velocity = 0
            if e.key == K_a and player.left:
                player.velocity = 0
            if e.key == K_w and player.up:
                player.velocity = 0
            if e.key == K_s and player.down:
                player.velocity = 0

    screen.fill(black)
    player.update() # Updates player in game loop
    player.draw(screen) # Draws player to screen in game loop
    for bullet in currentWeapon.bullets: # For every bullet in the bullet list it:
         bullet.draw(screen) # Draws bullet to screen
    playershealthbar.draw(screen) # Draws healthbar to screen
    display.update()

# bug 2 - Bullets would move in wrong direction
# fix 2 - Move bullet movement to projectile class and make a seperate update function for it
