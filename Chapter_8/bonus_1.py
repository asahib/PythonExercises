def multiplication_table(n):
  output = ""
  for a in range(n+1):
    for b in range(n+1):
      num = a*b
      output = output + '%5s'% str(num)
    output = output + "\n"
  return output

number = int(input("Please enter a number so that I can print the multiplication table :"))
print(multiplication_table(number))
 