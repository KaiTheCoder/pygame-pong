class PongBot():

    def __init__(self, gameAssets):
        ball, bot, paddle_speed = gameAssets

        self.ball = ball
        self.bot = bot
        self.paddle_speed = paddle_speed

    def update(self):
        self.ballY = self.ball.rect.y 
        self.botY = self.bot.rect.y

        if self.ballY > self.botY:
            self.bot.MoveUp(self.paddle_speed)
        if self.ballY  < self.botY:
            self.bot.MoveDown(self.paddle_speed)
