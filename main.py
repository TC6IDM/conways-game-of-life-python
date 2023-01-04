# Author: Andrew Tissi
# Date: 5/30/21
# Conway's Game of life

def drawlines(w,h,size,screen):
	white=(255,255,255)
	for x in range(0, w, size):
		for y in range(0, h, size):
			rect = pygame.Rect(x, y, size, size)
			pygame.draw.rect(screen, white, rect, 1)

def drawboxes(a,size,screen):
	white=(255,255,255)
	for i in range(len(a)):
		for k in range(len(a[i])):
			if a[i][k]==1:
				pygame.draw.rect(screen, white, pygame.Rect(k*size, i*size, size, size))

def evolve(a,xblocks,yblocks):
	a2=copy.deepcopy(a)
	for i in range(len(a)):
		for k in range(len(a[i])):
			value=evaluate(i,k,a,xblocks,yblocks)
			if a2[i][k]==0 and value==3:
				a2[i][k]=1
			elif a2[i][k]==1 and (value<2 or value>3):
				a2[i][k]=0
	return a2
			
			
def evaluate(i,k,a,xblocks,yblocks):
	value=0
	surroundings=[
		[-1,-1],
		[-1,1],
		[1,-1],
		[1,1],
		[0,-1],
		[0,1],
		[1,0],
		[-1,0]
		]

	for c in range(len(surroundings)):
		LookupX=surroundings[c][0]
		LookupY=surroundings[c][1]
		if -1<i+LookupX<xblocks and -1<k+LookupY<yblocks:
			value+=a[i+LookupX][k+LookupY]
	return value
			
import pygame#imports the pygame library
import math
import time
import copy
xblocks=50
yblocks=50
size=10
w=xblocks*size
h=yblocks*size
running=1
black=(0,0,0)
white=(255,255,255)
screen = pygame.display.set_mode((w, h))#creates the screen
clock = pygame.time.Clock()#creates the clock
draw=0
a = [[0 for i in range(xblocks)]for j in range(yblocks)]
drawlines(w,h,size,screen)
pygame.display.flip()
start=0
generation=0
delay=0.2
print("press q to start simulation")
while running:#runs while the snake has more than 0 lives
	screen.fill(black)#fills the screen black
	
	for event in pygame.event.get():#loops through every event
		if start==0:
			if event.type == pygame.QUIT:#checks if the user wnats to quit
				running=0
			elif event.type == pygame.MOUSEBUTTONDOWN:
				x,y=event.pos
				if a[math.floor(y/size)][math.floor(x/size)]==0:
					a[math.floor(y/size)][math.floor(x/size)]=1
				drawboxes(a,size,screen)
				drawlines(w,h,size,screen)
				pygame.display.flip()
				draw=1
			elif event.type == pygame.MOUSEMOTION and draw==1:
				x,y=event.pos
				if a[math.floor(y/size)][math.floor(x/size)]==0:
					a[math.floor(y/size)][math.floor(x/size)]=1
				drawboxes(a,size,screen)
				drawlines(w,h,size,screen)
				pygame.display.flip()
			elif event.type == pygame.MOUSEBUTTONUP:
				draw=0
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
				start=1
				print("Generation:",generation)
				time.sleep(delay)
		
	if start==1:
		a=evolve(a,xblocks,yblocks)
		screen.fill(black)#fills the screen black
		drawlines(w,h,size,screen)
		drawboxes(a,size,screen)
		pygame.display.flip()
		generation+=1
		print("Generation:",generation)
		time.sleep(delay)

	# clock.tick(240)#delays, draws once every 60ms