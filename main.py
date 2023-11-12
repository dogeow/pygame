import pygame
import sys

pygame.init()

# 设置窗口
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Lego Figure Example")

# 设置颜色
black = (0, 0, 0)
yellow = (255, 255, 0)

# 游戏循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 渲染背景
    screen.fill((255, 255, 255))  # 白色背景

    # 画头部
    pygame.draw.circle(screen, yellow, (400, 150), 30)

    # 画身体
    pygame.draw.rect(screen, black, (385, 180, 30, 50))

    # 画左腿
    pygame.draw.rect(screen, black, (385, 230, 10, 30))

    # 画右腿
    pygame.draw.rect(screen, black, (405, 230, 10, 30))

    # 画左手臂
    pygame.draw.rect(screen, black, (375, 180, 10, 30))

    # 画右手臂
    pygame.draw.rect(screen, black, (415, 180, 10, 30))

    # 更新屏幕
    pygame.display.flip()
