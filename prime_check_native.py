def isPrime(n):
    for i in range (2, n):
        if n % i == 0:
            return False
    return True


print('Enter range:')
a, b = map(int, input().split())
primes = []
for i in range(a, b + 1):
    if isPrime(i):
        primes.append(i)
print('Primes:', primes)
