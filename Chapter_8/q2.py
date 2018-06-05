# Modify the walking turtle program so that rather than a 90 degree left or right turn the angle of the turn is determined randomly at each step.

import turtle              # 1. import the modules
import random

def move_random(t):
  t.left(random.randrange(-360,360,1))
  t.forward(50)

def is_in_screen(window, t):
  turtle_x = t.xcor() if t.xcor() > 0 else -1*t.xcor() 
  turtle_y = t.ycor() if t.ycor() > 0 else -1*t.ycor()

  window_width = window.window_width()
  window_height = window.window_height()

  # print("Window width ",window_width /2 , " Pixel Position X " ,  turtle_x)
  # print("window_height ",window_height, " Pixel Position Y", turtle_y )
  

  still_in = True

  if(turtle_x >= (window_width/2) or (turtle_y >= window_height/2)):
    still_in = False
  
  return still_in

def colluded(t1,t2):
  if(t1.xcor() == t2.xcor()) and (t1.ycor() == t2.ycor()):
    return False

  return True

wn = turtle.Screen()       # 2. Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3. Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                # 4. Move the turtles to their starting point
lance.up()

andy.goto(-100,20)
lance.goto(-100,-20)

andy.speed(10)
lance.speed(10)

while is_in_screen(wn, andy) and is_in_screen(wn, lance) and colluded(andy, lance):
  move_random(andy)
  move_random(lance)


wn.exitonclick()
