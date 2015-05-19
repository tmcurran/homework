__author__ = 'elric'

#Paying Debt Off In a Year

#Calculates the minimum fixed monthly payment needed
#in order to pay off a credit card balance within 12
#months.

balance = float(raw_input("Enter your outstanding credit card balance: "))
annualInterest = float(raw_input("Enter your annual interest rate as a decimal: "))

monthlyInterestRate = annualInterest / 12.0

# Initialise months variable

monthlyPayment = 0
initBalance = balance

while balance > 0:
    monthlyPayment += 10
    balance = initBalance
    months = 0

    while months < 12 and balance > 0:
        months += 1
        interest = monthlyInterestRate * balance
        balance -= monthlyPayment
        balance += interest

balance = round(balance,2)

print "RESULT"
print "Monthly payment to pay off debt in 1 year: ",monthlyPayment
print "Number of months needed: ",months
print "Balance: ",balance
