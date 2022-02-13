import pygame 

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

    x = property(get_x, set_x)
    y = property(get_y, set_y)

class Paddle(PongAsset):
    def __init__(self, size, color, surf_color):
        super().__init__(size, color, surf_color)

    def move_up(self, pixels):
        self.y -= pixels 

    def move_down(self, pixels):
        self.y += pixels

class Ball(PongAsset):
    def __init__(self, size, color, surf_color):
        super().__init__(size, color, surf_color)
        
        self.speed = 7
        self.velocity = {'x': self.speed, 'y': self.speed}

    def update(self):
        self.x += self.velocity['x']
        self.y += self.velocity['y']

    def reflect_x(self):
        self.velocity['x'] = -self.velocity['x']

    def reflect_y(self):
        self.velocity['y'] = -self.velocity['y']
   
    def bounce(self):
        self.velocity['x'] = -self.velocity['x']
        self.velocity['y'] = self.speed
