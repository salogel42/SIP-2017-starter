from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)

### Write your code below:
sides = 5
for i in range(sides):
  forward(100)
  left(360/sides)


# Close window on click.
exitonclick()
