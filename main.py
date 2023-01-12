from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.screensize(canvwidth=600, canvheight=600, bg="black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with Food ### use distance method
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect Collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect Collision with Tail
    for segment in snake.segments[1:-1]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    # if head collides with any segment in the tail:
        # trigger game_over

screen.exitonclick()
