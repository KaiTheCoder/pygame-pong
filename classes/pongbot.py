class BotManager():

    def __init__(self, gameAssets):
        ball, bot, paddle_speed = gameAssets

        self.ball = ball
        self.bot = bot
        self.paddle_speed = paddle_speed

    def update(self):
        if self.ball.get_y() > self.bot.get_y():
            self.bot.move_up(self.paddle_speed)
        if self.ball.get_y() < self.bot.get_y():
            self.bot.move_down(self.paddle_speed)
