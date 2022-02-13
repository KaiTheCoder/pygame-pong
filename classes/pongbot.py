class PongBot():

    def __init__(self, gameAssets):
        pong_ball, pong_player, pong_bot, paddle_speed = gameAssets

        self.pong_ball = pong_ball
        self.pong_player = pong_player
        self.pong_bot = pong_bot
        self.paddle_speed = paddle_speed 

    def update(self):
        if abs(self.pong_ball.rect.x - self.pong_bot.rect.x) >= 50 and self.pong_ball.rect.y > self.pong_bot.rect.y:
            self.pong_bot.MoveUp(self.paddle_speed)
        if abs(self.pong_ball.rect.x - self.pong_bot.rect.x) >= 50 and self.pong_ball.rect.y < self.pong_bot.rect.y:
            self.pong_bot.MoveDown(self.paddle_speed)

