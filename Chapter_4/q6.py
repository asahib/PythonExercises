# Write a program that asks the user for the number of sides, the length of the side, the color, and the fill color of a regular polygon

sides = int(input("Please enter the number of sides? "))
length = int(input("Please enter the length of the side? "))
color = input("Please enter the line color? ")
fill_color = input("Please enter the fill color? ")

import turtle

wn = turtle.Screen()

polygon = turtle.Turtle()
polygon.color(color)
polygon.pensize(10)
polygon.fillcolor(fill_color)
polygon.begin_fill()

for side in range(sides):
  polygon.forward(length)
  polygon.left(360/sides)

polygon.end_fill()

wn.exitonclick()