from config import *

class Button:
    def __init__(self, rect, font, text, color):
        self.rect = rect
        self.color = color
        self.text = text

        self.set_text(text, font)

    def clicked(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        return False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(self.text_surface, (self.rect.left + 5, self.rect.top + 5))

    def set_text(self, text, font):
        self.text = text
        self.text_surface = font.render(self.text, True, Color.BLACK)