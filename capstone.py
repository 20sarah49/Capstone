# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl
import random 

# Create Classes
class Player(spgl.Sprite):
	def __init__(self, shape, color, x, y, distance):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.distance = distance
		self.speed = 0.5
		self.y_destination = 0
		self.powerup = 0
				
	def move_up(self):
		if self.ycor() < 200:
			#self.goto(self.xcor(), self.ycor()+200)
			self.y_destination += 200
		else:
			self.y_destination = 200
			#self.goto(self.xcor(), 200)
		
	def move_down(self):
		if self.ycor() > -200:
			#self.sety(self.ycor() - self.speed)
			self.y_destination -= 200
		else:
			#self.goto(self.xcor(), -200)
			self.y_destination = -200
	
	def tick(self):
		# Move right
		self.setx(self.xcor() + self.speed)
		# Distance
		self.distance -= self.speed


		# Move the player
		if self.ycor() < self.y_destination:
			self.sety(self.ycor() + 10)
		elif self.ycor() > self.y_destination:
			self.sety(self.ycor() - 10)
			
		
	# Fireball shoot function
	def shoot_fireball(self):
		if self.powerup > 0:
			fireball = Fireball("circle", "orangered", player.xcor(), player.ycor())
			self.powerup -= 1
			print(self.powerup)
		
			# Make Fireball move
			fireball.tick()
			
	# Speed Lag
	def speedlag(self):
		self.speed -= 0.25
		canvas = spgl.turtle.getcanvas()
		canvas.after(2000, self.speed_to_normal)
		
	def speed_to_normal(self):
		self.speed += 0.25	
		
class Obstacle(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.speed = random.randint(3,6)
		self.lt(180)

	
	def tick(self):
		self.move()
		

			
	def move(self):
		self.fd(self.speed)
		
		# Make the obstacle come back on screen
		if self.xcor() <= -375:
			self.setx(random.randint(400, 600))
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
			
# Fire ball class	
class Fireball(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.speed = 6
		self.lt(0)
	
	def tick(self):
		self.move()
		
	def move(self):
		self.fd(self.speed)
		
		if self.xcor() >= 380:
			self.destroy()

# Create Functions

# Initial Game setup
game = spgl.Game(800, 600, "blue", "Capstone Project by Sarah T-B", 0)

# Create Sprites
player = Player("triangle", "mediumvioletred", -350, 0, 700)
sharks = []
powerups = []
seaweeds = []
y_cors = [-200, 0, 200]
# Create multiple sprites per class
for i in range(0,2):
	shark = Shark("square", "dimgray", random.randint(350, 600), random.choice(y_cors))
	sharks.append(shark)
	powerup = Powerup("square", "gold", random.randint(350, 600), random.choice(y_cors))
	powerups.append(powerup)
	seaweed = Seaweed("square", "seagreen", random.randint(350, 600), random.choice(y_cors))
	seaweeds.append(seaweed)
	
# Create Labels
distance_label = spgl.Label("Distance From Shore: {}".format(player.distance), "white", -380, 280)

# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_UP, player.move_up)
game.set_keyboard_binding(spgl.KEY_DOWN, player.move_down)
game.set_keyboard_binding(spgl.KEY_SPACE, player.shoot_fireball)

while True:
	game_over = False
    # Call the game tick method
	game.tick()

	# Move Obstacles
	for shark in sharks:
		shark.tick()
	for powerup in powerups:
		powerup.tick()
	for seaweed in seaweeds:
		seaweed.tick()
		
	player.tick()
	
	# Update Label 
	distance_label.update("Distance From Shore: {}".format(player.distance))
	
	# Check for collisions
	for sprite in game.sprites:
		if isinstance(sprite, Shark):
			if game.is_collision(sprite, player):
				sprite.goto(random.randint(350, 600), random.choice(y_cors))
				print("GAME OVER: SHARK COLLISION")
				game_over = True

		if isinstance(sprite, Powerup):
			if game.is_collision(sprite, player):
				sprite.goto(random.randint(350, 600), random.choice(y_cors))
				print("POWERUP COLLISION")
				player.powerup = 5

		if isinstance(sprite, Seaweed):
			if game.is_collision(sprite, player):
				sprite.goto(random.randint(350, 600), random.choice(y_cors))
				print("SEAWEED COLLISION")
				player.speedlag()

	# Check for Power-up and Shark Collisions
	for sprite1 in game.sprites:
		if isinstance(sprite1, Shark):
			for sprite2 in game.sprites:
				if isinstance(sprite2, Fireball):
					if game.is_collision(sprite1, sprite2):
						sprite1.goto(random.randint(350, 600), random.choice(y_cors))
						sprite2.destroy()
						print("SHARK AND FIREBALL")
	
	# Game over when Distance is 0
	if player.distance == 0 :
		print("GAME CLEAR")
		game_over = True

	# End game
	if game_over:
		break

	game.print_game_info()
	