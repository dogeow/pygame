import sys

import pygame


class Example:
    def __init__(self):
        pygame.init()

        size = width, height = 800, 600
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("标题")

        self.is_running = True
        self.clock = pygame.time.Clock()

    def run_game(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((233, 233, 233))

            pygame.display.flip()

            self.clock.tick(60)


if __name__ == '__main__':
    ai = Example()
    ai.run_game()
