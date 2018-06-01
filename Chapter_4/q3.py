# Write a program that prints even integers from 0 to 50.
# for number in range(51):
#   if number % 2 == 0:
#     print(number)

# for number in range(1,101,1):
#   if(number%15 == 0):
#     print("fizz-buzz")
#   elif(number%3 == 0):
#     print("fizz")
#   elif(number%5 == 0):
#     print("buzz")
#   else:
#     print(number)

# for n in range(101):
#   print("fizz-buzz"if n%15==0 else"fizz"if n%3==0 else"buzz"if n%5==0 else n)

for n in range(1,101):
  print(((((n,"buzz")[n%5==0]),"fizz")[n%3==0],"fizz-buzz")[n%15==0])


