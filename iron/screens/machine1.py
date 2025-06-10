from config import *
from ui.button import Button

class Machine1:
    def __init__(self):
        self.background = BRICK_WALL_WINDOWS_BLURRED
        self.surface = pygame.surface.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.rect = pygame.rect.Rect(250, 100, 700, 600)

        rect = pygame.rect.Rect(300, 600, 200, 50)
        self.button = Button(rect, CONSOLAS_20, 'Create compound', Color.BUTTON)

    def update(self, mouse_pos, left_mouse_down):
        if left_mouse_down:
            return self.button.clicked(mouse_pos)
        return False

    def draw(self):
        self.surface.blit(self.background, (0, 0))
        pygame.draw.rect(self.surface, Color.MACHINE, self.rect)
        self.button.draw(self.surface)

    def get_surface(self):
        return self.surface