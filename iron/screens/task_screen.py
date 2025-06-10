from config import *

class TaskScreen:
    def __init__(self):
        self.background = BRICK_WALL
        self.surface = pygame.surface.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw(self):
        self.surface.blit(self.background, (0, 0))

    def get_surface(self):
        return self.surface