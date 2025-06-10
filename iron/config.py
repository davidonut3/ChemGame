import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

LEFT_MOUSE_BUTTON = 1
MIDDLE_MOUSE_BUTTON =2
RIGHT_MOUSE_BUTTON = 3

ASSETS = 'iron/assets/'

pygame.font.init()
CONSOLAS_20 = pygame.font.SysFont('Consolas', 20)

BRICK_WALL = pygame.image.load(ASSETS + 'backgrounds/brick_wall.png')
BRICK_WALL_BLURRED = pygame.image.load(ASSETS + 'backgrounds/brick_wall_blurred.png')
BRICK_WALL_WINDOWS = pygame.image.load(ASSETS + 'backgrounds/brick_wall_windows.png')
BRICK_WALL_WINDOWS_BLURRED = pygame.image.load(ASSETS + 'backgrounds/brick_wall_windows_blurred.png')

class Color:
    BLACK = 'black'
    WHITE = 'white'
    BUTTON = 'darkseagreen3'
    MACHINE = 'azure3'