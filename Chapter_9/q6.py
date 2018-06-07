def testEqual(str1,str2):
  print(str1==str2)

def reverse(text):
  reverse_str=''
  for i in range(len(text)-1,-1,-1):
    reverse_str = f'{reverse_str}{text[i]}'
  return reverse_str

def mirror(text):
  return f'{text}{reverse(text)}'

testEqual(mirror('good'), 'gooddoog')
testEqual(mirror('Python'), 'PythonnohtyP')
testEqual(mirror(''), '')
testEqual(mirror('a'), 'aa')