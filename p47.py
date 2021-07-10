import time


def is_prime(n):
    #print("--- is_prime("+str(n)+")")

    if n==2 or n==3:
        return True

    if n%2==0 or n%3==0:
        return False

    i = 5
    while i*i <= n:
        if n%i==0 or n%(i+2)==0:
          return False
        
        i+=6

    return True


primes = []
for i in range(2, 1000):
    if is_prime(i):
        primes.append(i)


def distinct_factors(n):
    #factors = []
    distinct = 0
    #p = 2
    #while p <= n:
    for p in primes:
        q = n   # quoziente
        #if is_prime(p):
        if q%p == 0:
            distinct+=1

        while q%p == 0 and q > 1:
            q = q//p
            #factors.append(p)

        #p+=1

    return distinct


def factors(n):
    factors = []

    for p in primes:
        q = n   # quoziente

        while q%p == 0 and q > 1:
            q = q//p
            factors.append(p)
            
    return factors


t_0 = time.time()
consec = 0
n = 2*3*5*7
last = 3
while consec < 4:
    if distinct_factors(n) == 4:
        consec+=1
    else:
        consec = 0

    n+=1

print(time.time()-t_0)
print(n-4, n-3, n-2, n-1)
