from turtle import Screen
import time
from paddle1 import Paddle1
from ball import Ball
from scoreboard import Scoreboard
#screen setup
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
#paddle spawner

paddle1 = Paddle1((350,0))
paddle2 = Paddle1((-350,0))

ball = Ball()
scoreboard = Scoreboard()
#event listeners
screen.listen()
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")

#game starts.
playing = True
while playing == True:
    screen.update()
    time.sleep(0.005)
    #render scoreboard
    scoreboard.show_current_score()

    ball.move()
    #detect wall collision
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.wall_bounce()

    #detect paddle collision
    if ball.distance(paddle1) <= 50 and ball.x_dir > 0 and ball.xcor() >= 330:
        ball.paddle_bounce()
    if ball.distance(paddle2) <= 50 and ball.x_dir < 0 and ball.xcor() <= -330:
        ball.paddle_bounce()

    #detect goal and reset ball.
    if ball.xcor() >= 400:
        scoreboard.player1_scored()
        ball.reset_location()
    if ball.xcor() <= -400:
        scoreboard.player2_scored()
        ball.reset_location()


screen.exitonclick()
