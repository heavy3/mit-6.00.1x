def ndigits(x):
    # base case
    if x == 0:
        return 0
        
    # recursive case, 
    else:
        # -1 / 10 = -1 (in python), so we use abs
        return 1 + ndigits(abs(x / 10))