"""按键控制"""
import pygame
import sys

pygame.init()

SIZE = WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)

screen = pygame.display.set_mode(SIZE)

ball_image = pygame.image.load('../assets/images/ball.png')
ball_rect = ball_image.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keyPressed = pygame.key.get_pressed()
    if keyPressed[pygame.K_LEFT]:
        ball_rect.left -= 2
        if ball_rect.left <= 0:
            ball_rect.left = 0

    if keyPressed[pygame.K_RIGHT]:
        ball_rect.left += 2
        if ball_rect.left > WIDTH - ball_rect.width:
            ball_rect.left = WIDTH - ball_rect.width

    screen.fill(WHITE)
    screen.blit(ball_image, ball_rect)

    pygame.display.flip()
