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
    
#test
print(is_prime(7))
print(is_prime(10))
print(count)
