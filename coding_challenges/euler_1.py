# Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def multiples_of_3_and_5(num):
  sum = 0
  for i in range(num):
    if i%3 == 0 or i%5 == 0:
      sum += i
  return sum

def main():
  num = int(input("Please enter a number so that the system will display the sum of multiples of 3 and 5 below than number:"))
  print(multiples_of_3_and_5(num))

if __name__ == '__main__':
  main()


