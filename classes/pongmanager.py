import pygame
from pygame.constants import K_DOWN, K_UP
from paddle import Paddle
from ball import PongBall

BACKGROUND_COLOR = (60, 50, 168)
OTHER_COLOR = (255,255,255)

MOVE_PIXELS = 7

class PongManager():
    def __init__(self):
        self.screenSize = (700, 500)
        self.screen = pygame.display.set_mode(self.screenSize)
        self.screenRect = self.screen.get_rect()

        self.paddleSize = [10, 130]
        self.paddleA = Paddle(self.paddleSize, OTHER_COLOR, BACKGROUND_COLOR)
        self.paddleB = Paddle(self.paddleSize, OTHER_COLOR, BACKGROUND_COLOR)
        
        self.paddleA.rect.x = 20
        self.paddleA.rect.y = 200

        self.paddleB.rect.x = 670
        self.paddleB.rect.y = 200

        self.ballSize = [15, 15]
        self.ball = PongBall(self.ballSize, OTHER_COLOR, BACKGROUND_COLOR)
        self.ball.rect.x = 30
        self.ball.rect.y = 205

        self.spritesList = pygame.sprite.Group()
        self.spritesList.add(self.paddleA)
        self.spritesList.add(self.paddleB)
        self.spritesList.add(self.ball)

        self.clock = pygame.time.Clock()
        self.gameActive = True


    def run(self):
        while self.gameActive: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.gameActive = False 
            
            self.keys = pygame.key.get_pressed()
            if self.keys[pygame.K_UP]:
                self.paddleA.MoveUp(MOVE_PIXELS)
            elif self.keys[pygame.K_DOWN]:
                self.paddleA.MoveDown(MOVE_PIXELS)

            self.paddleA.rect.clamp_ip(self.screenRect)
            self.paddleB.rect.clamp_ip(self.screenRect)
            self.ball.rect.clamp_ip(self.screenRect)

            self.spritesList.update()
        
            self.screen.fill(BACKGROUND_COLOR)
            self.spritesList.draw(self.screen)
       
            pygame.draw.line(self.screen, OTHER_COLOR, [349, 0], [349,500])

            pygame.display.update()

            self.clock.tick(60)
