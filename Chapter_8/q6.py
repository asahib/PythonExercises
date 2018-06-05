# Write a program to remove all the red from an image. (#BellPic.jpg)
from PIL import Image

img = Image.open("BellPic.jpg")

for row in range(img.height):
  for col in range(img.width):
    r,g,b = img.getpixel((col,row))
    img.putpixel((col,row),(0,g,b))

img.show()


