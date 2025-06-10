import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

ASSETS = 'iron/assets/'

BRICK_WALL = pygame.image.load(ASSETS + 'backgrounds/brick_wall.png')
BRICK_WALL_BLURRED = pygame.image.load(ASSETS + 'backgrounds/brick_wall_blurred.png')