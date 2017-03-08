balance = 3926
annualInterestRate = 0.2

lowestPayment = 0
totalPayment = 0
 
while True:   
    totalPayment = 0
    lowestPayment += 10
    remainBalance = balance
    for month in range(1, 13):  
        totalPayment += lowestPayment
        remainBalance = (remainBalance - lowestPayment)
        remainBalance = remainBalance + remainBalance * annualInterestRate / 12
    print(lowestPayment)
    if remainBalance <= 0 or lowestPayment >= balance:
        break
   
print('Lowest Payment: ' + str(lowestPayment))
print(totalPayment)
