__author__ = 'elric'

# Paying Off Credit Card Debt

# Problem 1: Paying the Minimum
# Calculates the credit card balance after one year
# if a person only pays the minimum monthly payment
# required by the credit card company each month.

balance = float(raw_input("Enter your outstanding balance: "))
annualInterestRate = float(raw_input("Enter your Annual Interest Rate (decimal): "))
minMonthlyPaymentRate = float(raw_input("Enter your minimum monthly payment rate (decimal): "))

# Minimum monthly payment
minMonthlyPayment = minMonthlyPaymentRate * balance

# Monthly Interest Rate
monthlyInterestRate = annualInterestRate / 12


month = 1
totalPaid = 0

while month < 13:
   #Minimum monthly payment of balance at start of the month
   minMonthlyPayment = round(minMonthlyPaymentRate * balance, 2)
   totalPaid += minMonthlyPayment

   #Amt of monthly payment that goes to interest
   interestPaid = round(monthlyInterestRate * balance, 2)

   #Amt of principal paid off
   principalPaid = minMonthlyPayment - interestPaid

   #Update remaining balance
   balance -= principalPaid


   print "Month: " + str(month)
   print "Minimum monthly payment: $" + str(minMonthlyPayment)
   print "Principal paid: $" + str(principalPaid)
   print "Remaining balance: $" + str(balance)

   #Count this as a new month
   month += 1

print "RESULT"
print "Total amount paid: $", totalPaid
print "Remaining balance: $", balance


