from string import ascii_lowercase, ascii_uppercase

def encrypt(strng, sub_str):
  encrypted = '' 

  for char in strng: 
    ascii_no = ord(char.lower())

    if(char in ascii_lowercase): 
      encrypted = f'{encrypted}{sub_str[ascii_no-97]}'

    elif(char in ascii_uppercase): 
      encrypted = f'{encrypted}{sub_str[ascii_no-97].upper()}' 

    else:
      encrypted = f'{encrypted}{char}' 
  
  return encrypted

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
