def testEqual(str1, str2):
  print(str1==str2)

class Car:

  def __init__(self,intitial_amount):
    self.gas_level = intitial_amount
  
  def add_gas(self,amounts):
    self.gas_level += amounts
  
  def fill_up(self):
    gas_necessary = 13.0 - self.gas_level
    if gas_necessary > 0:
      self.add_gas(gas_necessary)
      return gas_necessary
    else:
      return 0
  
def main():
  example_car = Car(9)
  print(example_car.fill_up())  # should print 4

  another_car = Car(18)
  print(another_car.fill_up()) # should print 0

  testEqual( Car(10).fill_up(), 3 )
  testEqual( Car(20).fill_up(), 0 )
  testEqual( Car(5.5).fill_up(), 7.5 )
  testEqual( Car(12.5).fill_up(), 0.5 )
  testEqual( Car(13).fill_up(), 0 )

if __name__ == '__main__':
  main()
