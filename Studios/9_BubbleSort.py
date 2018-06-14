def testEqual(a,b):
  print(a==b)

def bubble_sort(alist):
  is_sorted = False
  while is_sorted == False:
    num_swaps = 0
    for i in range(len(alist)-1):
      if alist[i] > alist[i+1]:
        temp = alist[i]
        alist[i] = alist[i+1]
        alist[i+1] = temp
        num_swaps += 1
    if num_swaps == 0:
      is_sorted = True
  return alist

testEqual(bubble_sort([0]), [0])  # Sorts a single element, returns same list
testEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])  # Sorted list is the same
testEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
testEqual(bubble_sort([4, 5, 3, 1, 2]), [1, 2, 3, 4, 5])
