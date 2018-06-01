# A sprite is a simple spider shaped thing with n legs coming out from a center point. The angle between each leg is 360 / n degrees.

# Write a program to draw a sprite where the number of legs is provided by the user.

import turtle

wn = turtle.Screen()
spider = turtle.Turtle()



legs = int(input("How many legs should this sprite have? "))
angle = 360/legs
spider.shape("triangle")
for i in range(legs):
  spider.right(angle)
  spider.forward(65)
  spider.stamp()
  spider.backward(65)
spider.shape("circle")

wn.exitonclick()
