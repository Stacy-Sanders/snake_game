from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.screensize(600, 600, "black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()

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
        print("nom nom nom")
        food.refresh()

screen.exitonclick()
