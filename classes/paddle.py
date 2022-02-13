import pygame

class Paddle(pygame.sprite.Sprite):

    def __init__(self, size, color, surfColor):
        super().__init__()
        
        self.score = 0

        self.image = pygame.Surface(size)
        self.image.fill(surfColor)
        self.image.set_colorkey(surfColor)

        pygame.draw.rect(self.image, color, [0,0] + size)

        self.rect = self.image.get_rect()

    def MoveUp(self, pixels):
        self.rect.y -= pixels

    def MoveDown(self, pixels):
        self.rect.y += pixels

    def SetScore(self, score):
        self.score = score
