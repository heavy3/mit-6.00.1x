balance = 320000
annualInterestRate = 0.2

appr = 0.000001
lower = balance / 12.0
upper = (balance * (1 + annualInterestRate / 12)**12) / 12.0
lowestPayment = (upper + lower) / 2 
while True:   
    remainBalance = balance
    for month in range(1, 13):  
        remainBalance = (remainBalance - lowestPayment)
        remainBalance = remainBalance + remainBalance * annualInterestRate / 12
    if remainBalance < 0:
        upper = lowestPayment
        lowestPayment = (upper + lower) / 2
    elif remainBalance > balance * appr:
        lower = lowestPayment
        lowestPayment = (upper + lower) / 2
    else:
        break
print('Lowest Payment: ' + str(round(lowestPayment, 2)))
