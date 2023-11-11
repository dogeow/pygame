"""加载图片"""
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))

ball_image = pygame.image.load('../images/ball.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(ball_image, (100, 200))

    pygame.display.flip()
