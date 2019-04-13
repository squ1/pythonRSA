#Generates prime numbers from x up to x

def primeNumberGenerator(x):
    primeNumbers = []                   
    for prime in range(2, x):           
        isPrime = True                  
        for test in range(2, prime):    
            if prime % test == 0:       
                isPrime = False         
                break                   
        if isPrime == True:
            if prime < 10:  #Change if you want prime to be at least x high
                continue            
            primeNumbers.append(prime)  
    return primeNumbers                
