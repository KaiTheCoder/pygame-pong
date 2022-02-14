import pygame 
from random import randint

class BotManager():

    def __init__(self, gameAssets):
        ball, bot = gameAssets

        self.ball = ball
        self.bot = bot
        self.paddle_speed = 6 

    def update(self):

        if self.bot.y < self.ball.y:
            self.bot.move_down(self.paddle_speed)
        if self.bot.y > self.ball.y: 
            self.bot.move_up(self.paddle_speed)

