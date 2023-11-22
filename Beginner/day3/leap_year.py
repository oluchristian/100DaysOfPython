#Checks if it's a leap year or not
year = int(input("Year? "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 ):
  print("It is a leap year")
else:
  print("It is not a leap year")
