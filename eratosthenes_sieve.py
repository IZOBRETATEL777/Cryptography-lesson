def eratosthenes(n):
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(2*i, len(sieve), i):
                sieve[j] = 0
    return sieve


print('Enter range:')
a, b = map(int, input().split())
primes = []
isPrime = eratosthenes(b)
for i in range(a, b + 1):
    if isPrime[i]:
        primes.append(i)
print('Primes:', primes)
