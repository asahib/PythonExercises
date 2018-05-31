P = 10000
n = 12
r = 8/100
t = int(input("Enter the number of years "))
print("The final amount after %s year(s) is %0.2f" % (t, P*(1+(r/n))**(n*t)))