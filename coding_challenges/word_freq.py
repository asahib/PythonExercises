# Write a function that outputs a word frequency dictionary
# format word: count, string:int
# should accept any text as an argument

def word_frequency(strg):
  word_count_dict = dict()
  char_count_dict = dict()
  for word in strg.split():
    word_count_dict[word] = (word_count_dict[word] + 1) if (word_count_dict.get(word,False)) else 1
  for char in strg:
    char_count_dict[char] = (char_count_dict[char] + 1) if (char_count_dict.get(char,False)) else 1
  return (word_count_dict, char_count_dict)

def print_counts(dict):
  for key, value in dict.items():
    print(key, " : ", value)

def main():
  sentence = input("Enter any input string \n")
  word_counts, char_counts = word_frequency(sentence)
  option = int(input("Please enter an option 1, 2 or 3\n 1. Word Count\n 2. Char Count\n 3. Both\nEnter option here"))
  if option==1:
    print_counts(word_counts)
  elif option==2:
    print_counts(char_counts)
  else:
    print_counts(word_counts)
    print_counts(char_counts)
    
if __name__ == '__main__':
  main()
