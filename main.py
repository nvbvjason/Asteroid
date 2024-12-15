import pygame
from player import Player
from constants import * 

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while (True):
        screen.fill(color="black")
        
        player.draw(screen)
        player.update(dt)

        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()

if __name__ == "__main__":
    main()
