__author__ = 'elric'

#Using Bisection Search to Make the Program Faster

#Calculates the minimum fixed monthly payment needed
#in order to pay off a credit card balance within 12
#months.

balance = float(raw_input("Enter your outstanding credit card balance: "))
annualInterest = float(raw_input("Enter your annual interest rate as a decimal: "))

monthlyInterestRate = annualInterest / 12.0

# Initialise months variable

initBalance = balance

low = balance / 12.0
high = (balance * (1 + monthlyInterestRate) ** 12.0) / 12.0
monthlyPayment = (low + high) / 2


while balance > 0 and monthlyPayment <= high:
    balance = initBalance
    months = 0

    while months < 12 and balance > 0:
        months += 1
        interest = monthlyInterestRate * balance
        balance -= monthlyPayment
        balance += interest

    if months > 12:
        monthlyPayment += 100

    elif balance < 0:
        monthlyPayment -= 100




balance = round(balance,2)

print "RESULT"
print "Monthly payment to pay off debt in 1 year: ",monthlyPayment
print "Number of months needed: ",months
print "Balance: ",balance
