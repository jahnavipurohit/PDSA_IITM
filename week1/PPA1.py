'''Twin primes are pairs of prime numbers that differ by 2. 
For example (3, 5), (5, 7), and (11,13) are twin primes.
Write a function Twin_Primes(n, m) where n and m are positive integers and n < m , 
that returns all unique twin primes between m and n (both inclusive). 
The function returns a list of tuples and each tuple (a,b) represents one unique twin prime where n <= a < b <= m.'''

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def Twin_Primes(n, m):
    twin_primes = []
    for i in range(n, m - 1):  # check pairs (i, i+2)
        if is_prime(i) and is_prime(i + 2) and i + 2 <= m:
            twin_primes.append((i, i + 2))
    return twin_primes

n=int(input())
m=int(input())
print(sorted(Twin_Primes(n, m)))