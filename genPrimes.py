def genPrimes():
    ''' Generator for a squence of primes number x where (x % p) != 0, where p
    is  a list of previous prime number'''
    primes = []
    p = 1
    while True:
        p += 1
        for prime in primes:
            if p % prime == 0:
                break
        else: # else lies here, wtf
            primes.append(p)
            yield p
        
