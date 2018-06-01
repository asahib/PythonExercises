import turtle              # 1. import the modules
import random

wn = turtle.Screen()       # 2. Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3. Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # 4. Move the turtles to their starting point
lance.up()
andy.goto(-100,20)
lance.goto(-100,-20)
andy.speed(1)
lance.speed(1)

# your code goes here
for i in range(48):
  if i%2 == 0:
    andy.forward(i)
  else:
    lance.forward(i)

wn.exitonclick()