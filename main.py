import pygame
pygame.init()

#from classes.pongmanager import PongManager 

from classes.paddle import Paddle
from classes.ball import PongBall

#pong = PongManager()
#pong.run()

# Constants
SURF_COLOR = (60, 50, 168) 
SPRITE_COLOR = (255, 255, 255)
SCREEN_SIZE = (700, 500)
PADDLE_SIZE = [10, 130]
BALL_SIZE = [10,10]

# Set up display
screen = pygame.display.set_mode(SCREEN_SIZE)
screenX = screen.get_width()
screenY = screen.get_height()

# Set up game assets
sprites_list = pygame.sprite.Group()

pong_player = Paddle(PADDLE_SIZE, SPRITE_COLOR, SURF_COLOR)
pong_bot = Paddle(PADDLE_SIZE, SPRITE_COLOR, SURF_COLOR)
pong_ball = PongBall(BALL_SIZE, SPRITE_COLOR, SURF_COLOR)

pong_player.rect.x = 20
pong_player.rect.y = screenY - 300 

pong_bot.rect.x = screenX - 20
pong_bot.rect.y = screenY - 300

pong_ball.rect.x = screenX / 2 
pong_ball.rect.y = screenY / 2

sprites_list.add(pong_player)
sprites_list.add(pong_bot)
sprites_list.add(pong_ball)

# Setup game loop 
running = True 
clock = pygame.time.Clock()

def process_input():
    

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
