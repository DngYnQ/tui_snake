import os
import random
import threading
import time
import keyboard
#🍏

mode = "hard" #easy,hard

game = True

keys = ["w", "a", "s", "d"]

class Map:
	def __init__(self):
		self.map        = []
		self.item_char  = "@"
		self.x          = 0
		self.y          = 0
		self.item_cords = []
		self.snake = []

	def gen(self,x,y):
		self.x = x
		self.y = y
		map = []
		for i in range(0,y+1):
			list = []
			for b in range(0,x+1):
				list.append(" ")
			map.append(list)
		self.map = map

	def draw(self):
		self.gen(self.x, self.y)
		for i in self.item_cords:
			self.map[i[1]][i[0]] = self.item_char
		for i in self.snake.snake[:self.snake.length]:
			self.map[i[1]][i[0]] = self.snake.snake_char

		print("#"+"-"*len(self.map[0])+"#")
		for i in self.map:
			result = ""
			for b in i:
				result+=b
			print(f"|{result}|")
		print("#"+"-"*len(self.map[0])+"#")

	def place(self, count=1):
		for i in range(0,count):
			rndy = random.randint(0,self.y)-2
			rndx = random.randint(0,self.x)-2

			if rndx <=-1:
				rndx=0
			if rndy <=-1:
				rndy=0

			self.item_cords.append([rndx, rndy])

def gameStop():
	global game
	game = False
	os.system("cls")
	print(f"\nLOSEER\n Length: {snake.length}")

class Snake:
	def __init__(self, map):
		self.snake_char = "#"
		self.length = 2
		self.map = map
		self.snake=[[int(map.x/2), int((map.y/2)-2)], [int(map.x/2), int((map.y/2)-1)]]
	def move(self, where):
		if where == "w":
			if self.snake[0][1] >= 1:
				self.snake.insert(0, [self.snake[0][0], self.snake[0][1]-1])
			else:
				if mode == "hard":
					gameStop()
		if where == "s":
			if self.snake[0][1] <= self.map.y-1:
				self.snake.insert(0, [self.snake[0][0], self.snake[0][1]+1])
			else:
				if mode == "hard":
					gameStop()
		if where == "a":
			if self.snake[1][0]-1 != 0:
				self.snake.insert(0, [self.snake[0][0]-1, self.snake[0][1]])
			else:
				if mode == "hard":
					gameStop()
		if where == "d":
			if self.snake[1][0] <= self.map.x-2:
				self.snake.insert(0, [self.snake[0][0]+1, self.snake[0][1]])
			else:
				if mode == "hard":
					gameStop()
		if self.snake[0] in self.map.item_cords:
			self.length+=1
			self.map.item_cords.remove(self.snake[0])
			self.map.place()
map = Map()

map.gen(21,10)

snake = Snake(map)

map.snake = snake

move = "stay"

map.place(2)

def listenKeyboard():
	global move
	def print_pressed_keys(e):
		global move
		if e.name in keys:
			move = e.name
	keyboard.hook(print_pressed_keys)
	keyboard.wait()

def game():
	while game:
		os.system("cls")
		map.draw()
		print(f"length: {snake.length}")
		#print(f"X: {snake.snake[0][0]}/{map.x}\nY: {snake.snake[0][1]}/{map.y}")
		snake.move(move)
		time.sleep(0.1)

threading.Thread(target=listenKeyboard).start()
threading.Thread(target=game).start()