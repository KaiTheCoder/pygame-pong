import time

class GameManager():
    def __init__(self, screen, game_assets):
        self.ball, self.player, self.bot = game_assets 

        self.ballY = self.ball.y
        self.ballX = self.ball.x 

        self.playerX = self.player.x 
        self.playerY = self.player.y 

        self.botX = self.bot.x 
        self.botY = self.bot.y  

    def reset(self):
        self.ball.x = self.ballX 
        self.ball.y = self.ballY

        self.player.x = self.playerX 
        self.player.y = self.playerY 

        self.bot.x = self.botX 
        self.bot.y = self.botY  



