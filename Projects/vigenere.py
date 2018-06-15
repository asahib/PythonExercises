from helpers import alphabet_position, rotate_character 
from sys import argv, exit

def vigenere_encrypt(text, key):
  a_list = [char for char in text]
  a_key = [char for char in key]
  a_key_index = 0
  new_list = [] 
  for item in a_list:
    if item.isalpha():
      encrypt_rotate = alphabet_position(a_key[a_key_index])
      new_list.append(rotate_character(item,encrypt_rotate))
      a_key_index = (a_key_index+1)%len(key)
    else:
      new_list.append(item)
  return ''.join(item for item in new_list)

def main():
  try:
    if not argv[1].isalpha():
      raise ValueError
    encryption_key = str(argv[1])
    message = input("Type a message: \n")
    print(vigenere_encrypt(message, encryption_key))
  except ValueError:
    print('usage: python vigenere.py keyword\n       Arguments:\n          -keyword : The string to be used as a "key" to encrypt your message.\n                     Should only contain alphabetic characters-- no numbers or special characters.')
  except IndexError:
    print('usage: python vigenere.py keyword\n      Arguments:\n          -keyword : The string to be used as a "key" to encrypt your message.\n                      Should only contain alphabetic characters-- no numbers or special characters.')
  

if __name__ == '__main__':
  main()
