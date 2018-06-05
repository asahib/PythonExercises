def string_pig_latin(str):
  words = str.split()
  new_str = ""
  vowels = ['a','e','i','o','u']
  for word in words:

    if word[0] in vowels:
      first_char = ''
      j = 0
      
    else:
      first_char = word[0]
      j = 1

    for i in range(j,len(word)):
      print(new_str)
      new_str=new_str+word[i]

    new_str = new_str+first_char+"ay "
  return new_str

print(string_pig_latin("all open androids"))
print(string_pig_latin("python code wins"))