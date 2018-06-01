# Write a program to draw some kind of picture. Be creative and experiment with the turtle methods provided in Summary of Turtle Methods.

import turtle

wn = turtle.Screen()
picture = turtle.Turtle()
picture.hideturtle()

for i in range(500):
  picture.forward(i)
  picture.right(98)

wn.exitonclick()