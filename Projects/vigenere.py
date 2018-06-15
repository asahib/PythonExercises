from helpers import alphabet_position, rotate_character 

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
  message = input("Type a message: \n")
  encryption_key = input("Encryption key: \n")
  print(vigenere_encrypt(message, encryption_key))


if __name__ == '__main__':
  main()
