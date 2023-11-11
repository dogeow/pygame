import sys

import pygame


class Example:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("examples")

    def run_game(self):

        ball_image = pygame.image.load('images/ball.png')

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()


            # 背景色
            self.screen.fill((233, 233, 233))
            # Surface
            self.screen.blit(ball_image, (100, 100))

            pygame.display.flip()


if __name__ == '__main__':
    ai = Example()
    ai.run_game()
