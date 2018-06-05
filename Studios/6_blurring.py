# Write a program to remove all the red from an image. (#BellPic.jpg)
from PIL import Image
from random import randrange

img = Image.open("BellPic.jpg")

width = img.width
height = img.height

newimg = Image.new('RGB',(width,height))

for row in range(1,height-1):
  for col in range(1,width-1):
    rand_col = col + randrange(-1,2)
    rand_row = row + randrange(-1,2)
    a = img.getpixel((rand_col,rand_row))
    newimg.putpixel((col,row),a)

img.show()
newimg.show()

