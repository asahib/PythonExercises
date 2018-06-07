from string import ascii_lowercase, ascii_uppercase

def encrypt(strng, sub_str):
  ciphered = '' # Initializing a variable to store the cipher text
  for char in strng: # Loopin through each character of the string to find and replace it with the appropriate cipher
    if(char in ascii_lowercase): #To handle the lower case letter
      ciphered = f'{ciphered}{sub_str[ord(char)-97]}' # replacing the lower case letter with corressponding case
    elif(char in ascii_uppercase): #To handle the upper case letter and 
      ascii_number = ord(sub_str[ord(char)-65])
      ciphered = f'{ciphered}{chr(ascii_number-32)}' # replacing the upper case letter with corressponding case
    else:
      ciphered = f'{ciphered}{char}' # If the char is not a valid Alphabet then using the same char
  # Retrun the cipher string
  return ciphered

def decrypt(strng,sub_str):
  decrypted = ''
  for char in strng:

    if(char in ascii_lowercase):
      decrypted = f'{decrypted}{ascii_lowercase[sub_str.find(char)]}'

    elif(char in ascii_uppercase):
      decrypted = f'{decrypted}{ascii_uppercase[(sub_str.upper()).find(char)]}'

    else:
      decrypted = f'{decrypted}{char}'
  return decrypted

print(encrypt('Good Days Are Comming','qwertyuiopasdfghjklzxcvbnm'))
encr= encrypt('Good Days Are Comming','qwertyuiopasdfghjklzxcvbnm')
print(decrypt(encr,'qwertyuiopasdfghjklzxcvbnm'))
