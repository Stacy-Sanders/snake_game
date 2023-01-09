from turtle import Screen, Turtle

# snake = Turtle()
screen = Screen()
screen.screensize(600, 600, "black")
screen.title("Snake Game")


x = 0
for snake_index in range(0, 3):
    snake = Turtle("square")
    snake.color("white")
    snake.setposition(x, 0)
    x -= 20













screen.exitonclick()
