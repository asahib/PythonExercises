# Printing the ith Element

# The function below, print_every(i, nums) receives a list of numbers nums, along with an integer i. 
# The function is supposed to print every ith element from the list. But it’s not working!

# in a list of numbers, print every ith number
def print_every(i, nums):
  counter = 0
  for j in nums:
    if counter % i == 0:
        print(j)
    counter += 1

# print_every(3, [4, 7, 2, 10, 1, 0, 9, 6])

def testEqual(bool1, bool2):
  print(bool1==bool2)

# return True if every member of the group is at least 70, otherwise return False
def check_group(ages):
  for age in ages:
    if age < 70:
        return False
  return True

# # this group should not be allowed inside the bar
# group = [78, 71, 25, 84]
# testEqual(check_group(group), False)

# # this group should also not be allowed inside the bar
# group2 = [ 2, 99 ]
# testEqual(check_group(group2), False)

# # this loner is allowed
# group3 = [ 99 ]
# testEqual(check_group(group3), True)

def password_checker(password):

# """
# A valid password has no spaces,
# and at least one non-alphabetical character
# """
  contains_non_alpha = False
  for char in password:
    if char == " ":
        return False
    elif not char.isalpha():
        contains_non_alpha = True
  return contains_non_alpha

# pw1 = "i <3 makonnen"
# print(password_checker(pw1))
# # should print False

# pw2 = "puzzlesareforfun"
# print(password_checker(pw2))
# # should print False

# pw2 = "puzzlesr4fun"
# print(password_checker(pw2))
# # should print True

def stretch(strng, num):
  list = [i for i in strng]
  new_strng=''.join([item*num for item in list])
  return new_strng

print(stretch("chihuahua", 2))