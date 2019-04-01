# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl

# Create Classes
class Player(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		
class Obstacle(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
	
# Create Functions

# Initial Game setup
game = spgl.Game(800, 600, "blue", "Capstone Project by Sarah G.", 0)

# Create Sprites
player = Player("circle", "white", -100, 0)
obstacle = Obstacle("square", "red", 100, 0)

# Create Labels

# Create Buttons

# Set Keyboard Bindings

while True:
    # Call the game tick method
    game.tick()
