import sys

import pygame


class Example:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((400, 300),)
        pygame.display.set_caption("标题")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((233, 233, 233))

            pygame.display.flip()


if __name__ == '__main__':
    ai = Example()
    ai.run_game()
