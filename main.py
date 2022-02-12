import pygame
pygame.init()

from classes.paddle import Paddle
from classes.ball import PongBall

# Constants
SURF_COLOR = (60, 50, 168) 
SPRITE_COLOR = (255, 255, 255)

SCREEN_SIZE = (600, 400)
PADDLE_SIZE = [10, 130]
BALL_SIZE = [10,10]

MOVE_PIXELS = 7

# Set up display
screen = pygame.display.set_mode(SCREEN_SIZE)
screenX = screen.get_width()
screenY = screen.get_height()
screenArea = screen.get_rect()

# Set up game assets
sprites_list = pygame.sprite.Group()

pong_player = Paddle(PADDLE_SIZE, SPRITE_COLOR, SURF_COLOR)
pong_bot = Paddle(PADDLE_SIZE, SPRITE_COLOR, SURF_COLOR)
pong_ball = PongBall(BALL_SIZE, SPRITE_COLOR, SURF_COLOR)

pong_player.rect.x = 20
pong_player.rect.y = screenY - 300 

pong_bot.rect.x = screenX - 20
pong_bot.rect.y = screenY - 300

pong_ball.rect.x = 30 
pong_ball.rect.y = 205

sprites_list.add(pong_player)
sprites_list.add(pong_bot)
sprites_list.add(pong_ball)

# Setup game loop 
running = True 
clock = pygame.time.Clock()

def process_input():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        pong_player.MoveUp(MOVE_PIXELS)
    elif keys[pygame.K_DOWN]:
        pong_player.MoveDown(MOVE_PIXELS)

def handle_ball():
    if pong_ball.rect.x >= screenX:
        pong_ball.bounceX()
    if pong_ball.rect.x <= 0:
        pong_ball.bounceX()
    if pong_ball.rect.y >= screenY:
        pong_ball.bounceY()
    if pong_ball.rect.y <= 0:
        pong_ball.bounceY()
    if pygame.sprite.collide_mask(pong_ball, pong_player) or pygame.sprite.collide_mask(pong_ball, pong_bot):
        pong_ball.bounce()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    process_input()
    handle_ball()

    pong_player.rect.clamp_ip(screenArea)
    pong_bot.rect.clamp_ip(screenArea)

    sprites_list.update()
    screen.fill(SURF_COLOR)
    sprites_list.draw(screen)

    pygame.draw.line(screen, SPRITE_COLOR, [screenX/2, 0], [screenX/2, screenY])
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
