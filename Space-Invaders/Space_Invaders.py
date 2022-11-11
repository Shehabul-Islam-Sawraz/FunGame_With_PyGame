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


# Placing the ship in the center from top 
# left (50 is used for centering the image as ship
# image is 100x100. So 50x50 is the middle) 
# at the start of the game
ship_x = WIDTH/2 - 50
ship_y = HEIGHT/2 - 50
# This angle will help to rotate the ship. Inititally
# the ship is faced to right. So angle=0
ship_angle = 0

# Canvas Declaration
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32) # Creating the screen
pygame.display.set_caption('Space Invaders') # Giving title to the screen

# Load Images
bg = pygame.image.load(os.path.join('images','bg.jpg'))
debris = pygame.image.load(os.path.join('images','debris.png'))
ship = pygame.image.load(os.path.join('images','ship.png'))

# Function to rotate an image at specified angle
def rot_center(image, angle):
    """rotate a Surface, maintaining position."""

    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

# Draw Game on Canvas
def draw(canvas):
    global time
    canvas.fill(BLACK) # Setting canvas with black
    canvas.blit(bg,(0,0)) # Adding background image on canvas
    canvas.blit(debris,(time*0.3,0)) # Showing debris on top of background
    canvas.blit(debris,(time*0.3-WIDTH,0)) # This helps to create a moving effect of debris
    time = time + 1
    canvas.blit(rot_center(ship,ship_angle), (ship_x, ship_y)) # Shows the ship at specified position & angle
    
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