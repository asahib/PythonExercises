# 10. Write a program to draw a face of a clock that looks something like this:

import turtle

wn = turtle.Screen()
clock = turtle.Turtle()
wn.bgcolor("light green")

clock.shape("turtle")
clock.color("blue")
clock.pensize(5)
clock.stamp()

for n in range(12):
  clock.penup()
  clock.forward(60)
  clock.pendown()
  clock.forward(5)
  clock.penup()
  clock.forward(20)
  clock.stamp()
  clock.forward(-85)
  clock.left(360/12)

wn.exitonclick()

