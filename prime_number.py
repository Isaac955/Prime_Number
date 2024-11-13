import random
from math import sqrt
def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
    
count = 0

for n in range(100,152):
    if is_prime(n):
        count = count + 1
    
def primes_in_range(start, end):
    primes = []
    for n in range(start, end + 1):
        if is_prime(n):
            primes.append(n)
    return primes

def count_in_range(start,end):
    count_primes = 0
    for n in range(start,end + 1):
        if is_prime(n):
            count_primes = count_primes + 1
    return count_primes

def generate_random_prime():
    while True:
        x = random.randint(2, 10**2)
        if is_prime(x):
            return x
#test
print(is_prime(7))
print(is_prime(10))
print(count)
print(primes_in_range(0,100))
print(count_in_range(0,100))
print(generate_random_prime())
