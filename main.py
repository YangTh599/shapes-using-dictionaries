import pygame, sys
import random
import math
import os
from os.path import join
from random import randint as rnd
from pygame.time import delay as slp

from colors import *
from pygame_config import *
import classes_and_objects.shapes as shapes

def init_game():
    pygame.init()
    pygame.display.set_caption(PYGAME_CAPTION) # Window Caption

    #Pygame Window
    window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    return window

# Draw Function to update graphics
def draw(window, shapes):
    
    window.fill(WHITE) # 15

    for shape in shapes:
        shape.draw()

    pygame.display.update()

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT
            return False
    
    return True

def main(): # MAIN FUNCTION
    window = init_game()
    clock = pygame.time.Clock()

    # ADD ALL OBJECTS/CLASSES BELOW HERE

    shapes_list = []

    
    # ADD ALL OBJECTS/CLASSES ABOVE HERE
    run = True
    while run: # run set to true, program runs while run is true.

        clock.tick(FPS) # FPS Tick

        run = handle_events()
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT: # QUIT
        #         run = False
        #         break
        

        shape_type = rnd(0,2)

        shape_options = {
            0 : shapes.Circ(window, rand_color(), (rnd(0,SCREEN_WIDTH), rnd(0,SCREEN_HEIGHT)),rnd(1,50)),
            1 : shapes.Rectangle(window, rand_color(), rnd(0,SCREEN_WIDTH), rnd(0,SCREEN_HEIGHT), rnd(10,100), rnd(10,100)),
            2 : shapes.Line(window, rand_color(), ((rnd(0,SCREEN_WIDTH), rnd(0,SCREEN_HEIGHT))), ((rnd(0,SCREEN_WIDTH), rnd(0,SCREEN_HEIGHT))), rnd(2,10))
        }

        new_shape = shape_options[shape_type]

        shapes_list.append(new_shape)

        draw(window, shapes_list) # UPDATES SCREEN

    pygame.quit()
    quit()
# ADD CLASSES HERE



# ADD CLASSES ABOVE
if __name__ == "__main__": 
    main()

