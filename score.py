from constants import *
import pygame

class Score(pygame.sprite.Sprite):
    containers = ()

    def __init__(self):
        super().__init__(self.containers)
        self.score = 0
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.color = (255, 255, 255) #"white"
        self.position = self.calculate_position()
    
    def calculate_position(self):
        dummy_text = self.font.render(f"Highscore: {self.score}", True, self.color)
        text_width = dummy_text.get_width()
        self.position = ((SCREEN_WIDTH - text_width - 10), 10)
        return self.position
    
    def draw(self, screen):
        text = f"Highscore: {self.score}"
        rendered_text = self.font.render(text, True, self.color)
        screen.blit(rendered_text, self.position) #draw {image} into {self.position}
    
    def update(self, dt):
        pass
