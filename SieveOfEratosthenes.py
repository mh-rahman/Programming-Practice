def SieveOfEratosthenes(n,req): 
    prime = [True for i in range(n+1)] 
    res, length = [], 0
    p = 2
    while (p * p <= n): 
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True):
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
      
    for p in range(2, n+1): 
        if prime[p]: 
            res.append(str(p))
            length += len(res[-1])
            if length > req+5:
                return res
    return [str(length)]

def solution(i):
    # Your code here
    primes = ''.join(SieveOfEratosthenes(25000,i))
    return primes[i:i+5]

print(solution(3))
print(solution(0))