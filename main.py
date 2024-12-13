import pygame
from constants import *
from player import Player
from circleshape import CircleShape

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_WIDTH))
    dt = 0 #delta time (time between frames)
    clock = pygame.time.Clock() #clock object
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        #checks if user closes the window, and if true quits teh screen
        screen.fill(color="black") #fills screen in solid black
        player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
        player.draw(screen)
        pygame.display.flip() #refreshes the screen
        dt = clock.tick(60)/1000 #uses clock objet to set max framerate to 60fps
        #tick method returns the delta time in milliseconds -> store it in dt in seconds


if __name__== "__main__":
    main()