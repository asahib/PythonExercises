class NewList:
  def __init__(self, lst):
    self.list = lst[:]
  
  def count(self, target):
    counter = 0
    for elem in self.list:
      counter += 1 if elem == target else 0
    return counter
  
  def is_in(self, target):
    for elem in self.list:
      if elem == target:
        return True 
    return False

  def reverse(self):
    reverse_list = ['']
    for i, elem in enumerate(self.list[::-1]):
      reverse_list.insert(i,elem)
    return reverse_list

  def index(self, target):
    for i, elem in enumerate(self.list):
      if str(elem) == str(target):
        return i
    return -1
  
  def insert(self,pos,value):
    newlist = []
    value = [value]
    if pos == 0:
      newlist = value[:] + self.list[:]
    elif pos > len(self.list):
      newlist = self.list[:]+value[:]
    else:
      newlist = self.list[:pos]+value[:]+self.list[pos:]
    return newlist

items = [1, "azhar", True, 5, 7, 8, 1, 1]
# items = items + "azhr"
myList = NewList(items)
print(myList.count(1))
print(myList.is_in(10))
print(myList.reverse())
print(myList.index(5))
items.insert(1,"test")
print(items)
print(myList.insert(100,"test"))

