from math import sqrt

def assert_equals(tuple1,tuple2):
    return True if (tuple1 == tuple2) else False

def isPrime(num):
  endRange = int(sqrt(num))+1
  for i in (range(2,endRange)):
    if num%i == 0:
      return False
  return True

def gap(diff, start, end):
  for i in range(start, end+1):
    if isPrime(i):
      firstPrime = i
      for j in range(i+1,end+1):
        if isPrime(j):
          if (j-firstPrime == diff):
            return [firstPrime, j]
          break
  return None


  '''
  primes = [item for item in range(start,end+1) if isPrime(item)]
  for i in range(len(primes)-1):
    if (primes[i+1] - primes[i]) == diff:
      return [primes[i],primes[i+1]]
    elif((primes[i+1] - primes[i]) == diff):
  '''
  return None

print(assert_equals(gap(2,100,110),[101,103]))
print(assert_equals(gap(4,100,110),[103,107]))
print(assert_equals(gap(6,100,110),None))
print(assert_equals(gap(8,300,400),[359,367]))
print(assert_equals(gap(10,300,400),[337,347]))


