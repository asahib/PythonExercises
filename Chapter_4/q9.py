# Drawing a star

import turtle

wn = turtle.Screen()
star = turtle.Turtle()

star.speed(1)
for i in range(5):
  star.left(144)
  star.forward(300)

wn.exitonclick()

