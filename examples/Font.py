import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))

font_size = 16

# print(pygame.font.get_fonts())

ff = pygame.font.SysFont('simsun', font_size)
# ff = pygame.font.Font(, font_size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))
    text = ff.render('你好，世界', True, (255, 255, 255), (255, 0, 0))
    screen.blit(text, (0, 0))
    pygame.display.flip()
