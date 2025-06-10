from config import *
from colors import Color
from screens.task_screen import TaskScreen

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('ChemGame')

task_screen = TaskScreen()

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    task_screen.draw()
    
    screen.fill(Color.WHITE)
    screen.blit(task_screen.get_surface(), (0, 0))

    pygame.display.update()
    clock.tick(60)

pygame.quit()