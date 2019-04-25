# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games
# Sounds from soundbible.com
# Background music from bensound.com

# Import SPGL
import spgl
import random 
import time

# Create Classes
class Player(spgl.Sprite):
	def __init__(self, shape, color, x, y, distance):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.distance = distance
		self.speed = 0.5
		self.y_destination = 0
		self.powerup = 0
		self.frame = 0
		self.frame_no = 0 
		self.frames = ["player1.gif", "player2.gif"]
		self.set_image(self.frames[self.frame_no], 80, 40)
				
	def move_up(self):
		if self.ycor() < 200:
			#self.goto(self.xcor(), self.ycor()+200)
			self.y_destination += 200
			game.play_sound("water-drop.wav")
		else:
			self.y_destination = 200
			#self.goto(self.xcor(), 200)
		
	def move_down(self):
		if self.ycor() > -200: 
			#self.sety(self.ycor() - self.speed)
			self.y_destination -= 200
			game.play_sound("water-drop.wav")
		else:
			#self.goto(self.xcor(), -200)
			self.y_destination = -200
	
	def tick(self):
		# Move right
		self.setx(self.xcor() + self.speed)
		# Distance
		# self.speed so that the distance decreases at a slower rate when the player collides with seaweed
		self.distance -= self.speed
		if self.distance%1 == 0:
			self.distance = int(self.distance)

		# Move the player
		if self.ycor() < self.y_destination:
			self.sety(self.ycor() + 10)
		elif self.ycor() > self.y_destination:
			self.sety(self.ycor() - 10)
			
		# Animate
		self.frame += 1
		if self.frame == 15:
			self.frame_no = 0
			self.set_image(self.frames[self.frame_no], 80, 40)
		elif self.frame == 30:
			self.frame_no = 1
			self.set_image(self.frames[self.frame_no], 80, 40)
		
		if self.frame > 30:
			self.frame = 0
		
		
			
		
	# Fireball shoot function
	def shoot_fireball(self):
		if self.powerup > 0:
			# Create fireball
			fireball = Fireball("circle", "orangered", player.xcor(), player.ycor())
			game.play_sound("shooting-star.wav")
			self.powerup -= 1
			print(self.powerup)
		
			# Make Fireball move
			fireball.tick()
			
	# Speed Lag
	def speedlag(self):
		self.speed = 0.5
		# Lag for .2 seconds
		canvas = spgl.turtle.getcanvas()
		canvas.after(2000, self.speed_to_normal)
		
	def speed_to_normal(self):
		self.speed = 1
		
	# Speed up 
	def speedup(self):
		self.speed = 1.5
		# Speed up for .2 seconds
		canvas = spgl.turtle.getcanvas()
		canvas.after(2000, self.speed_to_normal)
		
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
			self.speed = random.randint(3,6)
	
#Child Classes
class Shark(Obstacle):
	def __init__(self, shape, color, x, y):
		Obstacle.__init__(self, shape, color, x, y)	
		self.set_image("shark.gif", 40, 40)
		
class Powerup(Obstacle):
	def __init__(self, shape, color, x, y):
		Obstacle.__init__(self, shape, color, x, y)
		self.set_image("powerup.gif", 40, 40)
	
class Seaweed(Obstacle):
	def __init__(self, shape, color, x, y):
		Obstacle.__init__(self, shape, color, x, y)
		self.frame = 0
		self.frames = ["seaweed1.gif", "seaweed2.gif", "seaweed3.gif"]
		
	def tick(self):
		self.move()

		self.frame += 1
		if self.frame > len(self.frames)-1:
			self.frame = 0
			
		self.set_image(self.frames[self.frame], 40, 40)

class Fishingnet(Obstacle):
	def __init__(self, shape, color, x, y):
		Obstacle.__init__(self, shape, color, x, y)
		self.set_image("fishingnet.gif", 40, 40)

class Wave(Obstacle):
	def __init__(self, shape, color, x, y):
		Obstacle.__init__(self, shape, color, x, y)
		self.setheading(0)
		self.set_image("wave.gif", 40, 40)
	
	def move(self):
		self.fd(self.speed)
		
		if self.xcor() >= 380:
			self.setx(random.randint(-600, -400))
			y_cors = [-200, 0, 200]
			self.sety(random.choice(y_cors))
			self.speed = random.randint(3,6)
		
# Fire ball class	
class Fireball(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.speed = 6
		self.lt(0)
		self.frame = 0
		self.frames = ["fireball1.gif", "fireball2.gif", "fireball3.gif"]
	
	def tick(self):
		self.move()
		
		# Animate the fireballs
		self.frame += 1
		if self.frame > len(self.frames)-1:
			self.frame = 0
			
		self.set_image(self.frames[self.frame], 40, 40)
		
		
	def move(self):
		self.fd(self.speed)
		
		if self.xcor() >= 380:
			self.destroy()

# Initial Game setup
game = spgl.Game(800, 600, "blue", "Stuck at Sea! by Sarah T-B", 0)

# Create Sprites
player = Player("triangle", "mediumvioletred", -350, 0, 700.00)
sharks = []
powerups = []
seaweeds = []
fishingnets = []
y_cors = [-200, 0, 200]

# Create multiple sprites per class
for i in range(0,2):
	shark = Shark("square", "dimgray", random.randint(350, 600), random.choice(y_cors))
	sharks.append(shark)
	powerup = Powerup("square", "gold", random.randint(350, 600), random.choice(y_cors))
	powerups.append(powerup)
	seaweed = Seaweed("square", "seagreen", random.randint(350, 600), random.choice(y_cors))
	seaweeds.append(seaweed)
	
wave = Wave("square", "white", random.randint(-600, -350), random.choice(y_cors))

	
	
# Create Labels
distance_label = spgl.Label("Distance From Shore: {} // Fireballs: {}".format(player.distance, player.powerup), "white", -380, 280)
final_label = spgl.Label("", "red", -50, 0)

# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_UP, player.move_up)
game.set_keyboard_binding(spgl.KEY_DOWN, player.move_down)
game.set_keyboard_binding(spgl.KEY_SPACE, player.shoot_fireball)

# Set background image
game.set_background("bg.gif")

play_again_title = ""

game.play_sound("bensound-jazzyfrenchy.mp3", 105)

while True:
	game_over = False
	level2_access = False
    # Call the game tick method
	game.tick()

	# Move Obstacles
	for shark in sharks:
		shark.tick()
	for powerup in powerups:
		powerup.tick()
	for seaweed in seaweeds:
		seaweed.tick()
	for fishingnet in fishingnets:
		fishingnet.tick()

	wave.tick()
		
	player.tick()
	
	# Update Label 
	distance_label.update("Distance From Shore: {} // Fireballs: {}".format(player.distance, player.powerup))
	
	# Check for collisions
	for sprite in game.sprites:
		if isinstance(sprite, Shark):
			if game.is_collision(sprite, player):
				sprite.goto(random.randint(350, 600), random.choice(y_cors))
				print("GAME OVER: SHARK COLLISION")
				play_again_title = "GAME OVER: SHARK COLLISION"
				game_over = True

		elif isinstance(sprite, Powerup):
			if game.is_collision(sprite, player):
				sprite.goto(random.randint(350, 600), random.choice(y_cors))
				print("POWERUP COLLISION")
				player.powerup = 5

		elif isinstance(sprite, Seaweed):
			if game.is_collision(sprite, player):
				sprite.goto(random.randint(350, 600), random.choice(y_cors))
				print("SEAWEED COLLISION")
				player.speedlag()
		
		elif isinstance(sprite, Wave):
			if game.is_collision(sprite, player):
				sprite.goto(random.randint(-600, -350), random.choice(y_cors))
				print("WAVE COLLISION")
				player.speedup()
				
		elif isinstance(sprite, Fishingnet):
			if game.is_collision(sprite, player):
				sprite.goto(random.randint(-600, -350), random.choice(y_cors))
				print("FISHINGNET COLLISION")
				player.setx(-350)
				player.powerup = 0
				player.distance = 700.0
				

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
	if player.distance <= 0 :
		print("GAME CLEAR: Distance is zero")
		play_again_title = "GAME CLEAR: CONGRATULATIONS"
		game_over = True
		level2_access = True

	# End game
	if game_over:
		play_again = game.ask_yes_no(play_again_title, "Would you like to play again?")
		if play_again:
			player.setx(-350)
			player.powerup = 0
			player.distance = 700.0
			if level2_access:
				next_level = game.ask_yes_no("Next Level?", "Would you like to go to the next level?")
				if next_level:
					for i in range(0,2):
						fishingnet = Fishingnet("square", "dimgray", random.randint(350, 600), random.choice(y_cors))
						fishingnets.append(fishingnet)
					continue
				else:
					continue
		else:
			game.stop_all_sounds()
			break
			
	game.print_game_info()