# Write a function that implements a substitution cipher. In a substitution cipher one letter is substituted for another to garble the message. 
# For example A -> Q, B -> T, C -> G etc. your function should take two parameters, the message you want to encrypt, 
# and a string that represents the mapping of the 26 letters in the alphabet. Your function should return a string that is the encrypted version of the message.

def substitution_cipher(str, sub_str):
  ciphered = '' # Initializing a variable to store the cipher text

  for char in str: # Loopin through each character of the string to find and replace it with the appropriate cipher
    if((ord(char)>=97) and (ord(char)<=122)): #To handle the lower case letter
      ciphered = f'{ciphered}{sub_str[ord(char)-97]}' # replacing the lower case letter with corressponding case
    elif((ord(char)>=65) and (ord(char)<=90)): #To handle the upper case letter and 
      ciphered = f'{ciphered}{sub_str[ord(char)-65]}' # replacing the lower case letter with corressponding case
    else:
      ciphered = f'{ciphered}{char}' # If the char is not a valid Alphabet then using the same char

  # Retrun the cipher string
  return ciphered

print(substitution_cipher('Good days are comming','qwertyuiopasdfghjklzxcvbnm'))
