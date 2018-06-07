def get_initials(full_name):
  names = full_name.split()
  initials=''
  for name in names:
    initials=f'{initials}{name[0].upper()}'
  return initials

def name_validation(full_name):
  for i in range(len(full_name)):
    if(full_name[i]==' '):
      continue
    elif(not full_name[i].isalpha()):
      return False
  return True


def main():

  while True:
    fullname = input("What is your full name? \n")
    if(name_validation(fullname)):
      print(get_initials(fullname))
      break
    print("\nThe entered name has some invalid characters...\nOnly Alphabets and Spaces are allowed.. Please try again\n")
    continue

if __name__ == '__main__':
  main()

