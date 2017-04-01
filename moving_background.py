#file paths
background_image_filename = 'test_background.jpg'

import pygame
from pygame.locals import *
from sys import exit

#initialize pygame
pygame.init()

#set constants
SCREEN_SIZE = (800, 600)

#set display
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)

#load sprites
background = pygame.image.load(background_image_filename).convert() #convert_alpha() is used for curors

#set actual position on bckgrnd
x, y = 0, 0

#set distance to move
move_x, move_y = 0, 0

###Game Loop
while True:
	
	#manage events
	for event in pygame.event.get():

		##manage Quit event
		if event.type == QUIT:
			exit()

		##manage arrow keys

		#::VIDEORESIZE

		if event.type == VIDEORESIZE:
			SCREEN_SIZE = event.size
			screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
			pygame.display.set_caption("Window resized to "+str(event.size))

		#::KEY_DOWN
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
			 	move_x = -1
			elif event.key == K_RIGHT:
			 	move_x = +1
			elif event.key == K_UP:
				move_y = -1
			elif event.key == K_DOWN:
			 	move_y = +1
		
		#::KEY_UP
		elif event.type == KEYUP:
			if event.key == K_LEFT:
				move_x = 0
			elif event.key == K_RIGHT:
				move_x = 0
			elif event.key == K_UP:
				move_y = 0
			elif event.key == K_DOWN:
				move_y = 0

		x += move_x
		y += move_y

		screen.fill((0, 0, 0))
		screen.blit(background, (x, y))

		pygame.display.update()