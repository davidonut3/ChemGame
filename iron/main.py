from config import *
from screens.task_screen import TaskScreen
from screens.machine1 import Machine1

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('ChemGame')

task_screen = TaskScreen()
machine1 = Machine1()

left_mouse_down = False
at_machine = False

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == LEFT_MOUSE_BUTTON:
                left_mouse_down = True

    mouse_pos = pygame.mouse.get_pos()

    if at_machine:
        if machine1.update(mouse_pos, left_mouse_down):
            at_machine = False

        machine1.draw()
        screen.blit(machine1.get_surface(), (0, 0))
    else:
        if task_screen.update(mouse_pos, left_mouse_down):
            at_machine = True

        task_screen.draw()
        screen.blit(task_screen.get_surface(), (0, 0))

    left_mouse_down = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()