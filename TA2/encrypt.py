import random
import math

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n/2 +1)):
        if n % i == 0:
            return False
    return True

def generatePrime():
    prime = random.randint(2**8, 2**9)
    while not isPrime(prime):
        prime += 1
    return prime

def gcd(num1, num2):
    while num2 != 0:
        oldNum1 = num1
        num1 = num2
        num2 = oldNum1 % num2
    return num1

# BOILER
'''
Formula: num1 * s + num2 * t = gcd(num1, num2)
s, t are cofficients

S1, S2, T1, T2 are intermiditae coefficients
Standard Assumptions as per Euclidean Algorithem
S1 = 1  , S2= 0
T1 = 0, T2 = 1
'''
def extendedGCD(num1, num2, s1=1, s2=0, t1=0, t2=1):
    while num2 != 0:
        oldNum1 = num1
        num1 = num2
        num2 = oldNum1 % num2
        quotient = int(oldNum1/ num1)
        s = s1 - s2 * quotient
        t = t1 - t2 * quotient
        s1 = s2
        s2 = s
        t1 = t2
        t2 = t
    gcd = num1
    s = s1
    t = t1
    return s

def generateKeys():
    prime1 = generatePrime()
    prime2 = generatePrime()

    # Mutiply the prime numbers and store in variable 'modulus', that works as modulus in the public and private keys.
    

    # Subtract 1 from prime numbers and multiply them and store result in 'coprimeCount' variable.
    
    
    # Find random number between 2 and coprimeCount-1 and store result in 'publicExponent' variable.
    
    
    # Print the modulus, coprimeCount, publicExponent
    
    
generateKeys()

