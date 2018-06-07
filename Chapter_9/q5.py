def testEqual(str1,str2):
  print(str1==str2)

def is_palindrome(text):
  reverse_str=''
  for i in range(len(text)-1,-1,-1):
    reverse_str = f'{reverse_str}{text[i]}'
  return True if(reverse_str==text) else False
  

testEqual(is_palindrome('abba'), True)
testEqual(is_palindrome('abab'), False)
testEqual(is_palindrome('straw warts'), True)
testEqual(is_palindrome('a'), True)
testEqual(is_palindrome(''), True)

