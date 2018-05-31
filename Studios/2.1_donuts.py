# display welcome message to the user
print("Welcome to the Loop Hole! \nToday's Manager's Special is: \nCrunch Jelly: A traditional jelly donut in which the jelly filling is made entirely of Capn' Crunch Oops! All Berries")

# prompt the user for the number of donuts he likes
no_of_donuts = float(input("How many would you like? "))

# prompt the user for the price he wish to pay
price_per_donuts = float(input("How much would you like to pay per donut (suggested price is $4.35 each)? "))

# calculate the total price including the tax (5%)
total_price = no_of_donuts * price_per_donuts * 1.05

# display the price and thanks message to the user
print("Ok, let me prepare that for you....")
print("After tax, your total is: $%.2f" % total_price )
print("Thank you for snacking! Loop back around here soon!")