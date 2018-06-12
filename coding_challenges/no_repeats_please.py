# A Python program to print all 
# permutations using library function
from itertools import permutations
 
# Get all permutations of [1, 2, 3]

 
# Print the obtained permutations
def stamp_numbers(string):
  string = str(string)
  a_list = [item for item in string]
  for i in range(len(string)):
    a_list[i] = a_list[i] + str(i+1)
  return a_list

def permAlone(strng):
  perm = tuple(permutations(stamp_numbers(strng)))
  dict1 = {}
  for i in range(len(perm)):
    str1 = ''.join(item[0] for item in perm[i])
    str2 = ''.join(item for item in perm[i])
    flag = True
    for j in range(len(str1)-1):
      if str1[j] == str1[j+1]:
        flag = False
    if flag:
      dict1[str2] = str1
  print(len(dict1))
    
# perm = permutations(stamp_numbers('aab'))

# print(permAlone(tuple(perm)))

permAlone("aab") # should return 2.
permAlone("aaa") # should return 0.
permAlone("aabb") # should return 8.
permAlone("abcdefa") #  should return 3600.
permAlone("abfdefa") # should return 2640.
permAlone("zzzzzzzz") #  should return 0.
permAlone("a") #  should return 1.
permAlone("aaab") #  should return 0.
permAlone("aaabb") #  should return 12.


 

