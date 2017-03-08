balance = 5000
annualInterestRate = 0.18
monthlyPaymentRate = 0.02

minimumPayment = 0
totalPayment = 0
for month in range(1, 13):
    minimumPayment = balance * monthlyPaymentRate
    totalPayment += minimumPayment
    balance = (balance - minimumPayment)
    balance = balance + balance * annualInterestRate / 12
    print('Month: ' + str(month))
    print('Minimum monthly payment: ' + str(round(minimumPayment, 2)))
    print('Remaining balance: ' + str(round(balance, 2)))
    print(' ')

print('Total paid: ' + str(round(totalPayment, 2)))
print('Remaining balance: ' + str(round(balance, 2)))