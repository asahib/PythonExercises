from helpers import alphabet_position, rotate_character 
from sys import argv, exit

def encrypt(text, rot):
  a_list = [char for char in text]
  return ''.join(rotate_character(item,rot) for item in a_list)

def main():
  message = input("\nType a message \n")
  print(encrypt(message,int(argv[1])))

if __name__ == "__main__":
    main()