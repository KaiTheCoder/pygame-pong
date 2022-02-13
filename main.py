import pygame
pygame.init()

from classes.paddle import Paddle
from classes.ball import PongBall
from classes.pongbot import PongBot

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
pong_player2 = Paddle(PADDLE_SIZE, SPRITE_COLOR, SURF_COLOR)
pong_ball = PongBall(BALL_SIZE, SPRITE_COLOR, SURF_COLOR)

pong_player.rect.x = 20
pong_player.rect.y = screenY - 300 

pong_player2.rect.x = screenX - 20
pong_player2.rect.y = screenY - 300

pong_ball.rect.x = 30 
pong_ball.rect.y = 205

sprites_list.add(pong_player)
sprites_list.add(pong_player2)
sprites_list.add(pong_ball)

game_assets = [pong_ball, pong_player2, MOVE_PIXELS]
pong_bot = PongBot(game_assets)

# Setup game loop 
running = True 
clock = pygame.time.Clock()

player_score = 0
player2_score = 0
max_score = 11

debounce = True

def process_input():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        pong_player.MoveUp(MOVE_PIXELS)
    elif keys[pygame.K_DOWN]:
        pong_player.MoveDown(MOVE_PIXELS)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    process_input()

    # Make sure the ball doesn't go off screen
    if pong_ball.rect.x >= screenX and debounce == True:
        debounce = False 
        player_score += 1
        pong_ball.reflectX()
        debounce = True
    if pong_ball.rect.x <= 0 and debounce == True:
        debounce = False
        player2_score += 1
        pong_ball.reflectX()
        debounce = True
    if pong_ball.rect.y >= screenY or pong_ball.rect.y <= 0:
        pong_ball.reflectY()

    if pygame.sprite.collide_mask(pong_ball, pong_player) or pygame.sprite.collide_mask(pong_ball, pong_player2):
        pong_ball.bounce()

    # Prevent paddles from going off screen
    pong_player.rect.clamp_ip(screenArea) 
    pong_player2.rect.clamp_ip(screenArea)

    sprites_list.update()
    pong_bot.update()

    screen.fill(SURF_COLOR)
    sprites_list.draw(screen)

    font = pygame.font.Font(None, 74)
    text = font.render(str(player_score), 1, SPRITE_COLOR)
    screen.blit(text, (screenX/2/2, 10))

    text = font.render(str(player2_score), 1, SPRITE_COLOR)
    screen.blit(text, (screenX/2 + 100, 10))

    pygame.draw.line(screen, SPRITE_COLOR, [screenX/2, 0], [screenX/2, screenY])
    pygame.display.update()
    
    clock.tick(60)

pygame.quit()
