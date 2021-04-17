from math import gcd

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr


N = int(input())
data = list(map(int, input().split()))

is_pairwise_coprime = True
primes = set()
for val in data:
    divisors = factorization(val)
    for prime, _ in divisors:
        if prime in primes:
            is_pairwise_coprime = False
            break
        primes.add(prime)
    # print(divisors)

is_setwise_coprime = False
current_gcd = gcd(data[0], data[1])
for i in range(2, len(data)):
    current_gcd = gcd(current_gcd, data[i])

is_setwise_coprime = current_gcd == 1

if is_pairwise_coprime:
    print('pairwise coprime')
elif is_setwise_coprime:
    print('setwise coprime')
else:
    print('not coprime')
