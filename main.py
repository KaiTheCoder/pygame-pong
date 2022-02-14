import pygame
pygame.init()

#from classes.paddle import Paddle
#from classes.ball import PongBall
from classes.pongbot import BotManager 
from classes.pongassets import Paddle, Ball
from classes.gamemanager import GameManager

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
player = Paddle(PADDLE_SIZE, SPRITE_COLOR, SURF_COLOR)
player2 = Paddle(PADDLE_SIZE, SPRITE_COLOR, SURF_COLOR)
ball = Ball(BALL_SIZE, SPRITE_COLOR, SURF_COLOR)

player.x = 20
player.y = screenY - 300 

player2.x = screenX - 20
player2.y = screenY - 300

ball.x = 30  
ball.y = 205 

sprites_list = pygame.sprite.Group()

sprites_list.add(player)
sprites_list.add(player2)
sprites_list.add(ball)

bot_manager = BotManager([ball, player2, MOVE_PIXELS])
game_manager = GameManager(screen, [ball, player, player2])
# Setup game loop 
running = True 
clock = pygame.time.Clock()

player_score = 0
player2_score = 0

can_score = False

def process_input():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        player.move_up(MOVE_PIXELS)
    elif keys[pygame.K_DOWN]:
        player.move_down(MOVE_PIXELS)

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    process_input()

    if player_score == 11 or player2_score == 11:
        player_score = 0
        player2_score = 0

        game_manager.reset()


    # Make sure the ball doesn't go off screen
    if ball.x >= screenX:
        can_score = True
        
        if can_score:
            player_score += 1
            can_score = False
       
        ball.reflect_x()
    if ball.x <= 0:
        can_score = True 

        if can_score:
            player2_score += 1
            can_score = False
        
        ball.reflect_x()
    if ball.y >= screenY or ball.y <= 0:
        ball.reflect_y()

    if pygame.sprite.collide_mask(ball, player) or pygame.sprite.collide_mask(ball, player2):
        ball.bounce()

    # Prevent paddles from going off screen
    player.rect.clamp_ip(screenArea) 
    player2.rect.clamp_ip(screenArea)

    bot_manager.update()
    sprites_list.update()

    screen.fill(SURF_COLOR)
    sprites_list.draw(screen)

    font = pygame.font.Font(None, 74)
    text = font.render(str(player_score), 1, SPRITE_COLOR)
    screen.blit(text, (screenX/2/2, 10))

    text = font.render(str(player2_score), 1, SPRITE_COLOR)
    screen.blit(text, (screenX/2 + 100, 10))

    pygame.draw.line(screen, SPRITE_COLOR, [screenX/2, 0], [screenX/2, screenY])
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
