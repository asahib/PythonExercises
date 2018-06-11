# Write a function that outputs a word frequency dictionary
# format word: count, string:int
# should accept any text as an argument

def word_frequency(strg):
  dictionary = dict()
  for word in strg.split():
    dictionary[word] = (dictionary[word] + 1) if (dictionary.get(word,False)) else 1
  return dictionary

def main():
  sentence = input("Enter any input string \n")
  word_cout = word_frequency(sentence)
  for key, value in word_cout.items():
    print(key, " : ", value)

if __name__ == '__main__':
  main()