def get_initials(full_name):
  names = full_name.split()
  initials=''
  for name in names:
    initials=f'{initials}{name[0].upper()}'
  return initials

def name_validation(full_name):
  isblank = True
  for i in range(len(full_name)):
    if(full_name[i]==' '):
      continue
    elif(not full_name[i].isalpha()):
      return False
    else:
      isblank = False
  return True if (not isblank) else False


def main():

  while True:
    fullname = input("What is your full name? \n")
    if(name_validation(fullname)):
      print(get_initials(fullname))
      break
    print("\nThe entered name is invalid and might have some invalid characters...\nOnly Alphabets with Spaces are allowed.. Please try again\n")
    continue

if __name__ == '__main__':
  main()

