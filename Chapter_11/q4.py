def testEqual(str1,str2):
  print(str1==str2)

def translate(text):
  pirate_dict = {'sir':'matey',
                 'hotel':'fleabag inn',
                 'student':'swabbie',
                 'boy':'matey',
                 'madam':'proud beauty',
                 'professor':'foul blaggart',
                 'restaurant':'galley',
                 'your':'yer',
                 'excuse':'arr',
                 'students':'swabbies',
                 'are':'be',
                 'lawyer':'foul blaggart',
                 'restroom':"th' head",
                 'my':'me',
                 'hello':'avast',
                 'is':'be',
                 'man':'matey'
                }
  words=''
  new_str=''
  for char in text:
    if(char.isalpha()):
      words+=char
    else:
      new_str = new_str + pirate_dict.get(words,words) + char
      words=''
    # new_str = ' '.join([pirate_dict.get(item,item) for item in text.split() if item.isalpha()])
  return new_str

def main():
  text = "hello my man, please excuse your professor to the restroom!"
  testEqual(translate(text), "avast me matey, please arr yer foul blaggart to the th' head!")

if __name__ == '__main__':
  main()

