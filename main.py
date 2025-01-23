import turtle as t
import time
from paddle import Paddle
from ball import Ball
from score import ScoreBoard

screen = t.Screen()

screen.bgcolor('black')
screen.title('PONG')
screen.setup(width=800,height=600)

screen.tracer(0)

l_paddle = Paddle(-350,0)
r_paddle = Paddle(350,0)

ball = Ball()

score = ScoreBoard()

screen.listen()

screen.onkey(key='Up',fun=r_paddle.go_up)
screen.onkey(key='Down',fun=r_paddle.go_down)

screen.onkey(key='w',fun=l_paddle.go_up)
screen.onkey(key='s',fun=l_paddle.go_down)

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detects collision with wall.....
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce()

    # Detects collision with paddles.....
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_move += 2
        ball.bounceback()

    if ball.xcor() > 380:
        ball.reset_pos()
        score.update_l_score()
    elif ball.xcor() < -390:
        ball.reset_pos()
        score.update_r_score()
    score.score_display()
screen.exitonclick()