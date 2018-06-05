def print_triangular_numbers(num):
    triangular_number = 0
    for a in range (num):
        triangular_number += (a + 1)
        print(triangular_number)

def main():
  number = int(input("Please enter a number to find the triangular number? "))
  print_triangular_numbers(number)

if __name__ == "__main__":
  main()
  
