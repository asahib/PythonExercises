from helpers import alphabet_position, rotate_character 
from sys import argv, exit

def encrypt(text, rot):
  a_list = [char for char in text]
  return ''.join(rotate_character(item,rot) for item in a_list)

def main():
  encryption_no = 0
  try:
    encryption_no = int(argv[1])
    message = input("\nType a message \n")    
    print(encrypt(message,encryption_no))
  except ValueError:
    print("usage: python caesar.py n\n       where 'n' is a numeric")
  except IndexError:
    print("usage: python caesar.py n\n       where 'n' is a numeric")
  
if __name__ == "__main__":
    main()