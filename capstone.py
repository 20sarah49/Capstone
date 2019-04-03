# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl
import random 

# Create Classes
class Player(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		
	def move_up(self):
		if self.ycor() < 200:
			self.goto(self.xcor(), self.ycor()+200)
		else:
			self.goto(self.xcor(), 200)
		
	def move_down(self):
		if self.ycor() > -200:
			self.goto(self.xcor(), self.ycor()-200)
		else:
			self.goto(self.xcor(), -200)
		
class Obstacle(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.speed = 4
		self.lt(180)
	
	def tick(self):
		self.move()
			
	def move(self):
		self.fd(self.speed)
		
		
		if self.xcor() <= -375:
			self.setx(375)
			y_cors = [-200, 0, 200]
			self.sety(random.choice(y_cors))
	
#Child Classes
class Shark(Obstacle):
	def __init__(self, shape, color, x, y):
		Obstacle.__init__(self, shape, color, x, y)
		
		
		
class Powerup(Obstacle):
	def __init__(self, shape, color, x, y):
		Obstacle.__init__(self, shape, color, x, y)
	
class Seaweed(Obstacle):
	def __init__(self, shape, color, x, y):
		Obstacle.__init__(self, shape, color, x, y)
			
	
# Create Functions

# Initial Game setup
game = spgl.Game(800, 600, "blue", "Capstone Project by Sarah T-B", 0)

# Create Sprites
player = Player("circle", "white", -350, 0)
shark = Shark("square", "red", 350, 0)
powerup = Powerup("square", "orange", 350, -200)
seaweed = Seaweed("square", "grey", 350, 200)

# Create Labels

# Create Buttons

# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_UP, player.move_up)
game.set_keyboard_binding(spgl.KEY_DOWN, player.move_down)


while True:
    # Call the game tick method
	game.tick()

	shark.tick()
	powerup.tick()
	seaweed.tick()
	