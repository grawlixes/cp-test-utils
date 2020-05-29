import math

def divisors(n):
    sq = int(math.sqrt(n))
    return [(i, n // i) for i in range(1, sq + 1) if n % i == 0]

def isPrime(n):
    return len(divisorsOf(n)) == 1

def primesUpTo(n):
    primes = set(range(2, n + 1))
    for i in range(2, n):
        if i in primes:
            it = i * 2
            while it <= n:
                if it in primes:
                    primes.remove(it)
                it += i

    return primes

def getPrimeFactors(n):
    ret = {}
    sq = int(math.sqrt(n))
    primes = primesUpTo(n)
    
    for p in primes:
        if n in primes:
            ret[n] = 1
            break

        while n % p == 0:
            ret[p] = ret.get(p, 0) + 1
            n //= p
        
        if n <= 1:
            break

    return ret

def getInput():
    return open('input.txt', 'r').readlines()
