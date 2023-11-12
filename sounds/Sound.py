import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.mixer.music.load('../assets/sounds/大声说爱我 - 刘依纯.mp3')

# 设置音乐循环播放
pygame.mixer.music.set_volume(1)  # 设置音量（可选）
pygame.mixer.music.play(-1)  # -1 表示无限循环播放

ff = pygame.font.SysFont('simsun', 16)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not pygame.key.get_focused():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

    screen.fill((0, 0, 0))

    text = ff.render(str(pygame.mixer.music.get_pos()), True, (255, 255, 255))
    screen.blit(text, (0, 16))

    text = ff.render('当前', True, (255, 255, 255))
    screen.blit(text, (0, 0))

    pygame.display.flip()
