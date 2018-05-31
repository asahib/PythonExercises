# Write a program that prints out the lyrics to the song “99 Bottles of Beer on the Wall”

for bottle_no in range(10,-1,-1):
  if(bottle_no > 1):
    print(f'{bottle_no} bottles of beer on the wall, {bottle_no} bottles of beer.\nTake one down and pass it around, {bottle_no - 1} bottles of beer on the wall.\n')
  elif(bottle_no == 1):
    print(f'{bottle_no} bottle of beer on the wall, {bottle_no} bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n')
  else:
    print(f'No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.')
