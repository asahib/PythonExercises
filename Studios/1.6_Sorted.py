def is_sorted(string):
  for i in range(len(string)-1):
    if(string[i] > string[i+1]):
      return False
  return True

print(is_sorted("ABC"))
print(is_sorted("aBc"))
print(is_sorted("dog"))