import pygame, sys, os, random, math
from pygame.locals import *

pygame.init() # Initializing pygame
fps = pygame.time.Clock() # Recording frame per second for the graphics update

# Initializing Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

# Declaring height & width of the screen
WIDTH = 800
HEIGHT = 600      
time = 0

# Canvas Declaration
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32) # Creating the screen
pygame.display.set_caption('Space Invaders') # Giving title to the screen

# Load Images
bg = pygame.image.load(os.path.join('images','bg.jpg'))
debris = pygame.image.load(os.path.join('images','debris.png'))

# Draw Game on Canvas
def draw(canvas):
    global time
    canvas.fill(BLACK) # Setting canvas with black
    canvas.blit(bg,(0,0)) # Adding background image on canvas
    canvas.blit(debris,(time*0.3,0)) # Showing debris on top of background
    canvas.blit(debris,(time*0.3-WIDTH,0)) # This helps to create a moving effect of debris
    time = time + 1
    
# Handle Input
def handle_input():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()   

# Update Screen
def update_screen():
    pygame.display.update() # This updates the changes that we have done on draw function
    fps.tick(60)

# Game Control
while True:
    draw(window)
    handle_input()
    update_screen()