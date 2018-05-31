# Use for loops to make a turtle draw these regular polygons (regular means all no_of_sides the same lengths, all angles the same):
# Import Turtle
import turtle

wn = turtle.Screen()

#     An equilateral triangle
eq_triangle = turtle.Turtle()
eq_triangle.color("blue")
no_of_sides = 3
for side in range(no_of_sides):
  eq_triangle.forward(100)
  eq_triangle.left((360/no_of_sides))

#     A square
eq_triangle = turtle.Turtle()
eq_triangle.color("green")
no_of_sides = 4
for side in range(no_of_sides):
  eq_triangle.forward(100)
  eq_triangle.left((360/no_of_sides))

#     A hexagon (six no_of_sides)
eq_triangle = turtle.Turtle()
eq_triangle.color("red")
no_of_sides = 6
for side in range(no_of_sides):
  eq_triangle.forward(100)
  eq_triangle.left((360/no_of_sides))

#     An octagon (eight no_of_sides)
eq_triangle = turtle.Turtle()
eq_triangle.color("violet")
no_of_sides = 8
for side in range(no_of_sides):
  eq_triangle.forward(100)
  eq_triangle.left((360/no_of_sides))

wn.exitonclick()

