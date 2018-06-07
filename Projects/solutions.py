def get_initials(full_name):
  names = full_name.split()
  initials=''
  for name in names:
    initials=f'{initials}{name[0].upper()}'
  return initials

def main():
  fullname = input("What is your full name? \n")
  print(get_initials(fullname))

if __name__ == '__main__':
  main()

