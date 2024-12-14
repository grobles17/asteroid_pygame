import pygame
from constants import *
from player import Player
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_WIDTH))
    dt = 0 #delta time (time between frames)
    clock = pygame.time.Clock() #clock object
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        #checks if user closes the window, and if true quits teh screen
        
        for obj in updatable:
            obj.update(dt)
         

        screen.fill(color="black") #fills screen in solid black
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip() #refreshes the screen

        dt = clock.tick(60)/1000 #uses clock objet to set max framerate to 60fps
        #tick method returns the delta time in milliseconds -> store it in dt in seconds

if __name__== "__main__":
    main()