import pygame
#from random import randint

class PongBall(pygame.sprite.Sprite): 
    def __init__(self, size, color, surfColor):
        super().__init__()
        
        self.image = pygame.Surface(size)
        self.image.fill(surfColor)
        self.image.set_colorkey(surfColor) 

        pygame.draw.rect(self.image, color, [0,0] + size)

        self.rect = self.image.get_rect()
        self.speed = 7 

        self.velocity = {
            'x': self.speed, 
            'y': self.speed 
        }

    def update(self):
        self.rect.x += self.velocity['x']
        self.rect.y += self.velocity['y']

    def bounce(self):
        self.velocity['x'] = -self.velocity['x']
        self.velocity['y'] = self.speed 

    def reflectX(self):
        self.velocity['x'] = -self.velocity['x']

    def reflectY(self):
        self.velocity['y'] = -self.velocity['y']

