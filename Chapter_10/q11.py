# Write a function that will sum up all the elements in a list up to but not including the first even number.
def testEqual(s1,s2):
  print(s1, " | ", s2, " : ", s1==s2)

def sum_of_initial_odds(nums):
  sum = 0
  for item in nums:
    if item%2 == 0:
      break
    sum += item 
  return sum

testEqual(sum_of_initial_odds([1,3,1,4,3,8]), 5)
testEqual(sum_of_initial_odds([6,1,3,5,7]), 0)
testEqual(sum_of_initial_odds([1, -7, 10, 23]), -6)
testEqual(sum_of_initial_odds(range(1,555,2)), 76729)