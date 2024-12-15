import pygame
from player import Player
from shoots import Shoot
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group() 
    shoots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shoot.containers = (shoots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()

    while (True):
        screen.fill(color="black")
        dt = clock.tick(60) / 1000

        for drawa in drawable:
            drawa.draw(screen)
        for updatea in updatable:
            updatea.update(dt)
        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game over!")
                return
        for bullet in shoots:
            for asteroid in asteroids:
                if bullet.collides(asteroid):
                    bullet.kill()
                    asteroid.kill()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()

if __name__ == "__main__":
    main()
