import pygame
from pygame import Color, Rect
pygame.init()

BLACK = Color(0, 0, 0)

screen = pygame.display.set_mode([320, 480])
clock = pygame.time.Clock()
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(BLACK)
    
    pygame.display.flip()
    clock.tick(1)

pygame.quit()
