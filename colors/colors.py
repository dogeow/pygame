import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))

redColour = pygame.Color(255, 0, 0)
blackColour = pygame.Color(0, 0, 0)
whiteColour = pygame.Color(255, 255, 255)
greyColour = pygame.Color(150, 150, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))

    for i in range(4):
        pygame.draw.rect(screen, redColour, ((0, 0), (100, 100)))
        pygame.draw.rect(screen, blackColour, ((100, 0), (100, 100)))
        pygame.draw.rect(screen, whiteColour, ((200, 0), (100, 100)))
        pygame.draw.rect(screen, greyColour, ((300, 0), (100, 100)))

    pygame.display.flip()
