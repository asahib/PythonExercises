#Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
#If it is currently 13 and you set your alarm to go off in 50 hours, the hour will be 15 (3pm). Write a program to solve the general version of the above problem. Ask the user for the current time (in hours), and then ask for the number of hours to wait for the alarm.
#Your program should output what the hour will be on the clock when the alarm goes off.


current_time = int(input("What is the current time (in hours)? "))
waiting_time = int(input("How many hours do you have to wait before alarm goes off? "))

print("The Alarm will goes off on %s hour" % ((current_time + waiting_time)%24) )