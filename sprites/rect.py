import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.sprite.Sprite.image = pygame.Surface([100, 100])

    pygame.display.flip()
