import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
sound = pygame.mixer.Sound('../sounds/大声说爱我 - 刘依纯.mp3')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    sound.play()

    pygame.display.flip()
