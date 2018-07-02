from math import sqrt

def assert_equals(tuple1,tuple2):
    return True if (tuple1 == tuple2) else False

def isPrime(num):
  endRange = int(sqrt(num))+1
  for i in (range(2,endRange)):
    if num%i == 0:
      return False
  return True

def primeGaps(diff, start, end):
  initialPrime = 0
  secondPrime = 0
  for i in range(start,end+1):
    if(isPrime(i)):
      if((i-initialPrime) == diff):
        secondPrime = i
        return (initialPrime, secondPrime)
      else:
        initialPrime = i
  return None

print(assert_equals(primeGaps(2,100,110),(101,103)))
print(assert_equals(primeGaps(4,100,110),(103,107)))
print(assert_equals(primeGaps(6,100,110),None))
print(assert_equals(primeGaps(8,300,400),(359,367)))
print(assert_equals(primeGaps(10,300,400),(337,347)))


