# Draw this pretty pattern.

import turtle

def draw_square(length, angle):
  sqrt_t = turtle.Turtle()
  # sqrt_t.shape("circle")
  sqrt_t.hideturtle()
  sqrt_t.color("blue")
  sqrt_t.left(angle)
  for i in range(4):
    sqrt_t.forward(length)
    sqrt_t.left(90)

wn = turtle.Screen()

number_of_squares = 40
for i in range(0,360,int(360/number_of_squares)):
  draw_square(100,i)
wn.exitonclick()