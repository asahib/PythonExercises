def string_pig_latin(str):
  words = str.split()
  new_str = ""
  for word in words:
    for vowel in ['a','e','i','o','u']:
      if word[0] == vowel:
        first_char = ''
      else:
        first_char = word[0]
    for i in range(len(word)-1):
      new_str=new_str+word[i+1]
    new_str = new_str+first_char+"ay "
  return new_str

print(string_pig_latin("all open androids"))
print(string_pig_latin("python code wins"))