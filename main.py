#Starting
import pygame
import random
from copy import copy, deepcopy
import numpy as np
import heapq

pygame.init()
pygame.mixer.init()


#Game Classes
class Screen(object):
	def __init__(self, width, height):
		self.surface = pygame.display.set_mode((width,height), pygame.FULLSCREEN)
		self.width = width
		self.height = height


class GameMap(object):
	def __init__(self, map_name):
		self.file = open(map_name, 'r')
		global gmap
		global soundMap
		global gheight
		global gwidth
		global protected_blocks
		protected_blocks = ['#', 'g']
		gmap = []
		for line in self.file.readlines():
		    gmap.append([])
		    for i in list(line):
		        gmap[-1].append(i)
		soundMap = deepcopy(gmap)
		gheight = len(gmap)
		gwidth = len(gmap[0])
		self.name = map_name
		self.file.close()

	def Save(self):
		self.file = open(self.name, 'w')
		for i,line in enumerate(gmap):
			for j,ch in enumerate(line):
				if(i == player.rect.y and j == player.rect.x):
					self.file.write('p')
				else:
					self.file.write(ch)
		self.file.close()
		self.file = open(self.name, 'r')

	def Print(self,layer):
		#Printing

		#Getting Print Range Map Value
		y_range_min = int(((player.rect.y-(screen.height/2))/32)+player.rect.y)
		x_range_min = int(((player.rect.x-(screen.width/2))/32)+player.rect.x)

		if(y_range_min < 0):
			y_range_min = 0
		if(x_range_min < 0):
			x_range_min = 0

		y_range_max = int(y_range_min+((screen.height)/32))
		x_range_max = int(x_range_min+((screen.width)/32))

		if(y_range_max > gheight):
			y_range_max = gheight
		if(x_range_max > gwidth):
			x_range_max = gwidth



		if(layer == '0'):
			
			for i in range(y_range_min, y_range_max):
				for j in range(x_range_min, x_range_max):

			#for i in range(gheight):
				#for j in range(gwidth):

					#Setting The Layer Block Velocity
					layerXVel = ((screen.width/2)-16)+(((j-1)-player.rect.x)*32)
					layerYVel = (((screen.height/2)-16)+(i-player.rect.y)*32)


					#Printing Player In Center Of Screen:
					screen.surface.blit(player.sprite,((screen.width/2)-16,(screen.height/2)-16))
						
					
					if(gmap[i][j-1] == '#'):
						wall.set_alpha(60)
						imageVoid = pygame.transform.scale(wall, (18, 18))
						screen.surface.blit(imageVoid,(layerXVel+7,layerYVel+7))

					elif(gmap[i][j-1] == '/'):
						#screen.surface.blit(enemy,((j-1)*32,i*32))
						screen.surface.blit(door,(layerXVel,layerYVel))

					elif(gmap[i][j-1] == 'g'):
						#screen.surface.blit(enemy,((j-1)*32,i*32))
						screen.surface.blit(generator,(layerXVel,layerYVel))


		if(layer == '1'):
			for i in range(y_range_min, y_range_max):
				for j in range(x_range_min, x_range_max):

			#for i in range(gheight):
				#for j in range(gwidth):

					#Setting The Layer Block Velocity
					layerXVel = (((screen.width/2)-16)+(((j-1)-player.rect.x)*32)+(((j-1)-player.rect.x))*1.5)
					layerYVel = ((((screen.height/2)-16)+(i-player.rect.y)*32)+(((i)-player.rect.y)*1.5))
					
					#3D Walls (BETA)
					if(gmap[i][j-1] == '#'):
						wall.set_alpha(100)
						imageVoid = pygame.transform.scale(wall, (22, 22))
						screen.surface.blit(imageVoid,(layerXVel+5,layerYVel+5))

		if(layer == '2'):
			for i in range(y_range_min, y_range_max):
				for j in range(x_range_min, x_range_max):

			#for i in range(gheight):
				#for j in range(gwidth):

					#Setting The Layer Block Velocity
					layerXVel = (((screen.width/2)-16)+(((j-1)-player.rect.x)*32)+(((j-1)-player.rect.x)*3))
					layerYVel = ((((screen.height/2)-16)+(i-player.rect.y)*32)+(((i)-player.rect.y)*3))
					
					#3D Walls (BETA)
					if(gmap[i][j-1] == '#'):
						wall.set_alpha(160)
						imageVoid = pygame.transform.scale(wall, (26, 26))
						screen.surface.blit(imageVoid,(layerXVel+3,layerYVel+3))

		if(layer == '3'):
			for i in range(y_range_min, y_range_max):
				for j in range(x_range_min, x_range_max):

			#for i in range(gheight):
				#for j in range(gwidth):

					#Setting The Layer Block Velocity
					layerXVel = (((screen.width/2)-16)+(((j-1)-player.rect.x)*32)+(((j-1)-player.rect.x)*4.5))
					layerYVel = ((((screen.height/2)-16)+(i-player.rect.y)*32)+(((i)-player.rect.y)*4.5))
					
					#3D Walls (BETA)
					if(gmap[i][j-1] == '#'):
						wall.set_alpha(200)
						imageVoid = pygame.transform.scale(wall, (32, 32))
						screen.surface.blit(imageVoid,(layerXVel,layerYVel))

	def Generate():
		#function to generate a random map
		pass


class Player(object):
	def __init__(self,sprite):
		self.sprite = pygame.image.load(sprite).convert()
		self.up = True
		self.down = True
		self.left = True
		self.right = True
		self.walk_cooldown = 0
		self.speed = 0.6
		self.rect  = self.sprite.get_rect()

		#reading start position
		for i in range(gheight):
			for j in range(gwidth):
				if(gmap[i][j-1] == 'p'):
					self.rect.x = j-1
					self.rect.y = i
					gmap[i][j-1] = '.'

	def Movement(self):
		self.walk_cooldown -= speed_deacrese

		keys = pygame.key.get_pressed()

		if(self.walk_cooldown <= 0):
			
			if keys[pygame.K_w]:
				if(player.Collision('up') == False):
					self.rect.y -= 1
					self.walk_cooldown = self.speed

			elif keys[pygame.K_s]:
				if(player.Collision('down') == False):
					self.rect.y += 1
					self.walk_cooldown = self.speed

			elif keys[pygame.K_a]:
				if(player.Collision('left') == False):
					self.rect.x -= 1
					self.walk_cooldown = self.speed

			elif keys[pygame.K_d]:
				if(player.Collision('right') == False):
					self.rect.x += 1
					self.walk_cooldown = self.speed

	def Collision(self, side):
		#protected_blocks = ['#', 'g']

		if(side == 'up'):
			for i in protected_blocks:
				if(gmap[self.rect.y-1][self.rect.x] == i):
					return True

		elif(side == 'down'):
			for i in protected_blocks:
				if(gmap[self.rect.y+1][self.rect.x] == i):
					return True

		elif(side == 'right'):
			for i in protected_blocks:
				if(gmap[self.rect.y][self.rect.x+1] == i):
					return True

		elif(side == 'left'):
			for i in protected_blocks:
				if(gmap[self.rect.y][self.rect.x-1] == i):
					return True
		
		return False


#BETA enemies
class Enemy(object):
	def __init__(self):
		#Creating a Value Map of The Fase (Binery Map, 0 and 1)
		self.valueMap = deepcopy(gmap)
		for i in range(gheight):
			for j in range(gwidth):
				if(self.valueMap[i][j-1] in protected_blocks):
					self.valueMap[i][j-1] = 1
				else:
					self.valueMap[i][j-1] = 0

				if(i == gheight-1 and j == gwidth-1):
					self.valueMap[i].append(0)

	class Scoffer(object):
		#Enemy with aleatories Moves
		def __init__(self,sprite,x,y):
			self.sprite = pygame.image.load(sprite).convert()
			self.x = x
			self.y = y
			self.state = 0
			self.walk_cooldown = 0
			self.speed = 8
			self.rect  = self.sprite.get_rect()

		def Update(self):
			#Printing On Screen
			layerXVel = ((screen.width/2)-16)+(((self.x)-player.rect.x)*32)
			layerYVel = (((screen.height/2)-16)+(self.y-player.rect.y)*32)
			screen.surface.blit(self.sprite,(layerXVel,layerYVel))

			#Movimentation
			self.walk_cooldown -= speed_deacrese
			move = random.choice(['up', 'down', 'right', 'left'])
			if(self.Collision(move) == False and self.walk_cooldown <= 0):
				if(move == 'up'):
					self.y -= 1
					self.walk_cooldown = self.speed
				elif(move == 'down'):
					self.y += 1
					self.walk_cooldown = self.speed
				elif(move == 'right'):
					self.x += 1
					self.walk_cooldown = self.speed
				elif(move == 'left'):
					self.x -= 1
					self.walk_cooldown = self.speed

		def Collision(self, move):

			if(move == 'up'):
				for i in protected_blocks:
					if(gmap[self.y-1][self.x] == i):
						return True

			elif(move == 'down'):
				for i in protected_blocks:
					if(gmap[self.y+1][self.x] == i):
						return True

			elif(move == 'right'):
				for i in protected_blocks:
					if(gmap[self.y][self.x+1] == i):
						return True

			elif(move == 'left'):
				for i in protected_blocks:
					if(gmap[self.y][self.x-1] == i):
						return True
			
			return False

	class Clatter(object):
		#I´ts a Sound moving enemy
		def __init__(self,sprite,x,y):
			self.sprite = pygame.image.load(sprite).convert()
			self.x = x
			self.y = y
			self.state = 0
			self.walk_cooldown = 0
			self.speed = 2
			self.rect  = self.sprite.get_rect()
			self.route = []

		def Update(self):
			#Printing On Screen
			layerXVel = ((screen.width/2)-16)+(((self.x)-player.rect.x)*32)
			layerYVel = (((screen.height/2)-16)+(self.y-player.rect.y)*32)
			screen.surface.blit(self.sprite,(layerXVel,layerYVel))

			#Movimentation
			self.walk_cooldown -= speed_deacrese
			if(self.route == [] and self.route != False):
				start = (self.y,self.x)
				goal = (player.rect.y,player.rect.x)
				self.route = clatter.FindPath(start, goal)
				
			if(self.route != [] and self.route != False and self.walk_cooldown <= 0):
				self.y = int(self.route[0][0])
				self.x = int(self.route[0][1])
				self.route.pop(0)
				self.walk_cooldown = self.speed
				
		def heuristic(self, a, b):
			return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

		def FindPath(self, start, goal):
			array = np.array([enemy.valueMap[0]])
			for i in range(1, len(enemy.valueMap)):
				new_row = enemy.valueMap[i]
				array = np.append(array, [new_row], axis=0)

			neighbors = [(0,1),(0,-1),(1,0),(-1,0)]

			close_set = set()
			came_from = {}
			gscore = {start:0}
			fscore = {start:self.heuristic(start, goal)}
			oheap = []

			heapq.heappush(oheap, (fscore[start], start))

			while oheap:

			    current = heapq.heappop(oheap)[1]

			    if current == goal:
			        data = []
			        while current in came_from:
			            data.append(current)
			            current = came_from[current]
			        data += [start]
			        return data[::-1]

			    close_set.add(current)
			    for i, j in neighbors:
			        neighbor = current[0] + i, current[1] + j
			        tentative_g_score = gscore[current] + self.heuristic(current, neighbor)
			        if 0 <= neighbor[0] < array.shape[0]:
			            if 0 <= neighbor[1] < array.shape[1]:                
			                if array[neighbor[0]][neighbor[1]] == 1:
			                    continue
			            else:
			                # array bound y walls
			                continue
			        else:
			            # array bound x walls
			            continue
			            
			        if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
			            continue
			            
			        if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
			            came_from[neighbor] = current
			            gscore[neighbor] = tentative_g_score
			            fscore[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
			            heapq.heappush(oheap, (fscore[neighbor], neighbor))
			            
			return False



class Events(object):
	def __init__(self):
		self.runing = True

	def Handle(self):
		#Events
		for event in pygame.event.get():
			#Game Quit
			if(event.type == pygame.QUIT):
				self.runing = False

			#Game Menu Open
			elif(event.type == pygame.KEYDOWN):
				if(event.key == pygame.K_ESCAPE):
					gui.PauseMenu()

class GUI(object):
	def __init__(self):
		pass
	def PauseMenu(self):
		ch0.pause()
		ch1.play(pause_music, -1)
		menuRuning = True
		while menuRuning:
			for event in pygame.event.get():
				#Game Menu Quit
				if(event.type == pygame.KEYDOWN):
					if(event.key == pygame.K_ESCAPE):
						menuRuning = False
						ch0.unpause()
						ch1.fadeout(1000)

			pygame.draw.rect(screen.surface, [0, 0, 0], pygame.Rect(0, 0, screen.width, screen.height))
			resoursesBtn = gui.button((screen.width/2)-200,(screen.height/10)*3,400,40,'Resourses')
			saveBtn = gui.button((screen.width/2)-200,(screen.height/10)*4,400,40,'Save')
			menuBtn = gui.button((screen.width/2)-200,(screen.height/10)*5,400,40,'Main Menu')
			exitBtn = gui.button((screen.width/2)-200,(screen.height/10)*6,400,40,'Exit')

			
			resoursesBtn.Print()
			saveBtn.Print()
			menuBtn.Print()
			exitBtn.Print()

			if(resoursesBtn.Click() == True):
				print("Resourses")
			if(saveBtn.Click() == True):
				gameMap.Save()
			if(menuBtn.Click() == True):
				menuRuning = False
				gui.StartMenu()
				exit()
			if(exitBtn.Click() == True):
				pygame.quit()
				exit()

			#Updating Screen
			pygame.display.update()

	def StartMenu(self):
		background_image = pygame.image.load('assets/menu.png').convert()
		background_image = pygame.transform.scale(background_image,(screen.width,screen.height))
		menuRuning = True
		ch0.fadeout(1000)
		ch1.play(start_music, -1)
		while menuRuning:
			for event in pygame.event.get():
				#Game Menu Quit
				if(event.type == pygame.KEYDOWN):
					if(event.key == pygame.K_ESCAPE):
						menuRuning = False

			pygame.draw.rect(screen.surface, [0, 0, 0], pygame.Rect(0, 0, screen.width, screen.height))

			screen.surface.blit(background_image, [0, 0])


			playBtn = gui.button((screen.width/2)-200,(screen.height/10)*8,400,40,'PLAY')
			exitBtn = gui.button((screen.width/2)-200,(screen.height/10)*9,400,40,'EXIT')
			
			playBtn.Print()
			exitBtn.Print()

			if(playBtn.Click() == True):
				menuRuning = False
				main()
				exit()
			if(exitBtn.Click() == True):
				pygame.quit()
				exit()

			#Updating Screen
			pygame.display.update()

	class button(object):
		def __init__(self, x, y, width, height, text):
			self.x = x
			self.y = y
			self.width = width
			self.height = height
			self.text = text

		def Print(self):

			pygame.draw.rect(screen.surface, [255, 255, 255], pygame.Rect(self.x, self.y, self.width, self.height))
			font = pygame.font.SysFont('arial', 30)
			text = font.render(self.text, 1,(0,0,0))
			screen.surface.blit(text, ((self.x + (self.width/2 - text.get_width()/2)),(self.y + (self.height/2 - text.get_height()/2))))

		def Click(self):
			mouse = pygame.mouse.get_pos()
			if(mouse[0]>self.x and mouse[1]>self.y and mouse[0]<self.x+self.width and mouse[1]<self.y+self.height):
				if(pygame.mouse.get_pressed()[0] == 1):
					pygame.time.wait(100)
					return True
				return False
			return False


#Configurations\Loading
#screen = Screen(640,360)
#screen = Screen(720,480)
screen = Screen(1280, 720)
FPS = 30
pygame.display.set_caption("Terminus")
clock = pygame.time.Clock()
events = Events()
gui = GUI()

#Map Load
gameMap = GameMap('map.gmp')
wall  = pygame.image.load('assets/wall.png').convert()
door = pygame.image.load('assets/door.png')
generator = pygame.image.load('assets/generator.png')

#Player Load
player = Player('assets/player.png')

#Walk Speed Deacrese
speed_deacrese = FPS/100

#Enemies Load
enemy = Enemy()
clatter = enemy.Clatter('assets/clatter.png',1,1)
scoffer = enemy.Scoffer('assets/scoffer.png',1,10)
scoffer2 = enemy.Scoffer('assets/scoffer.png',16,18)

#Sound\Music Load\Configuration
ch0 = pygame.mixer.Channel(0) #Music channel 1
ch1 = pygame.mixer.Channel(1) #Music channel 2
ch2 = pygame.mixer.Channel(2) #Music channel 3
ch3 = pygame.mixer.Channel(3) #Empty
ch4 = pygame.mixer.Channel(4) #Sfx
ch5 = pygame.mixer.Channel(5) #Character sfx

ch0.set_volume(0.4)

switch_sfx = pygame.mixer.Sound("audio/sfx/switch.wav")

pause_music = pygame.mixer.Sound("audio/music/PauseMenu.wav")
start_music = pygame.mixer.Sound("audio/music/StartMenu.wav")
main_music = pygame.mixer.Sound("audio/music/MainGame.wav")


#Game
def main():
	ch1.fadeout(500)
	ch0.play(main_music, -1)
	while events.runing:
		#FPS
		clock.tick(FPS)
		
		#Filling Screen With Black
		screen.surface.fill([0, 0, 0])

		#Events on Game
		events.Handle()

		#Movimentation
		player.Movement()

		#Beta Enemys
		clatter.Update()
		scoffer.Update()
		scoffer2.Update()

		#Printing the Map
		gameMap.Print('0')
		gameMap.Print('1')
		gameMap.Print('2')
		gameMap.Print('3')

		
		#Screen Atualization
		
		#Quit/Loop Configs
		pygame.display.update()
	pygame.quit()

gui.StartMenu()