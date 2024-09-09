#Calculate total amount of an electric bill
kiloWat = int(input("Enter the KW hours used: "))
#Kilowat rates
first_1000_rate = 7.633
over_1000_rate = 9.258

if kiloWat <= 1000:
    totalWat = ("%.2f" % (kiloWat * first_1000_rate/100))
else:
    totalWat = ("%.2f" % (1000 * first_1000_rate/100 + (kiloWat - 1000) * over_1000_rate/100))

print("Amount owed is $"+totalWat)