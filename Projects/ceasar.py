from helpers import alphabet_position, rotate_character 

def encrypt(text, rot):
  a_list = [char for char in text]
  return ''.join(rotate_character(item,rot) for item in a_list)

def main():
  message = input("\nType a message \n")
  rotate = int(input("Rotate by :\n"))
  print(encrypt(message,rotate))

if __name__ == "__main__":
    main()