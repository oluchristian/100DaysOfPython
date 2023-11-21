#A simple tip calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
calc_percentage = float((percentage_tip/100)*bill)
people = int(input("How many people to split the bill? "))
total_bill = calc_percentage + bill
#Format the bill per person using round func & format specifier
bill_per_person = round((total_bill/people), 2)
formated_bill = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${formated_bill}")
