def likes(names):
  if len(names) == 0:
    return "No one like this"
  elif len(names) == 1:
    return names[0] + " likes this"
  elif len(names) == 2:
    return names[0] + " and "+ names[1] +" like this"
  elif len(names) ==  3:
    return names[0] + ", "+ names[1] + " and "+ names[2] +" like this"
  elif len(names) > 3:
    return names[0] + ", "+ names[1] + " and " + str(len(names)-2) + " others like this"

def main():
  list1=[]
  list2=["Azhar"]
  list3=["Azhar","Patrick"]
  list4=["Azhar","Patrick","Jeeva"]
  list5=["Azhar","Patrick","Jeeva","Shastri"]

  print(likes(list1))
  print(likes(list2))
  print(likes(list3))
  print(likes(list4))
  print(likes(list5))

if __name__ == '__main__':
  main()