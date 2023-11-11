import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
ff = pygame.font.SysFont('simsun', 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    text = ff.render(str(pygame.key.get_focused()), True, (255, 255, 255))

    screen.fill((0, 0, 0))

    screen.blit(text, (0, 0))

    pygame.display.flip()
