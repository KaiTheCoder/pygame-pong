import pygame 
import math

class PongAsset(pygame.sprite.Sprite):
    def __init__(self, size, color, surf_color):
        super().__init__()

        self.image = pygame.Surface(size)
        self.image.fill(surf_color)
        self.image.set_colorkey(surf_color)

        pygame.draw.rect(self.image, color, [0,0] + size)

        self.rect = self.image.get_rect()

    def set_x(self, x):
        self.rect.x = x 

    def set_y(self, y):
        self.rect.y = y 

    def get_x(self):
        return self.rect.x

    def get_y(self): 
        return self.rect.y

    def get_center(self):
        return self.rect.center 

    def set_center(self, center):
        self.rect.center = center

    x = property(get_x, set_x)
    y = property(get_y, set_y)

class Paddle(PongAsset):
    def __init__(self, size, color, surf_color):
        super().__init__(size, color, surf_color)

    def move_up(self, pixels):
        self.y -= pixels 

    def move_down(self, pixels):
        self.y += pixels

class VecBall(PongAsset):

    def __init__(self, size, color, surf_color):
        super().__init__(size, color, surf_color)
        
        self.angle = 45 
        self.speed = 12 

        self.velocity = { 
            'x': self.speed * math.cos(self.angle),
            'y': self.speed * math.sin(self.angle)
        }

    def update(self):
        self.x += self.velocity['x']
        self.y += self.velocity['y'] 

    def reflect_x(self): 
        self.velocity['x'] = -self.velocity['x']

    def reflect_y(self):
        self.velocity['y'] = -self.velocity['y']

    def bounce(self): 
        self.velocity['x'] = -self.velocity['x']
        self.velocity['y'] = -self.velocity['y']



