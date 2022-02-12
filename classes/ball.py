import pygame
from random import randint

class PongBall(pygame.sprite.Sprite): 
    def __init__(self, size, color, surfColor):
        super().__init__()
        
        self.image = pygame.Surface(size)
        self.image.fill(surfColor)
        self.image.set_colorkey(surfColor) 

        pygame.draw.rect(self.image, color, [0,0] + size)

        self.rect = self.image.get_rect()
        
        self.velocity = {
            'x': randint(-7, 7),
            'y': randint(-7, 7)
        }

    def update(self):
        self.rect.x += self.velocity['x']
        self.rect.y += self.velocity['y']

    def bounce(self):
        self.velocity['x'] = -self.velocity['x']
        self.velocity['y'] = randint(-7, 7)

    def bounceX(self):
        self.velocity['x'] = -self.velocity['x']

    def bounceY(self):
        self.velocity['y'] = -self.velocity['y']

