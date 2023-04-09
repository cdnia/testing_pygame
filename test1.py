import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First test pygame")
BACKGROUND_IMG = pygame.image.load("table_image.jpg").convert()
FRONT_IMG = pygame.image.load("a_pc_mouse_image.jpg").convert_alpha()
is_running = True


while is_running:
    # a loop on the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            pygame.quit()
            sys.exit()
        # This line uses the blit member function of the screen Surface object,
        # which takes a source image—in this case, our 640 x 480 background
        # and a tuple containing the destination position
        screen.blit(BACKGROUND_IMG, (0, 0))
        # mouse pointer
        x, y = pygame.mouse.get_pos()
        x = x - FRONT_IMG.get_width()/2
        y = y - FRONT_IMG.get_height()/2
        screen.blit(FRONT_IMG, (x, y))
        pygame.display.update()
