N = int(input())

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

divisors = make_divisors(2 * N)

count = 0
for x in divisors:
    y = (2*N) // x
    if x % 2 == 0 and y % 2 != 0:
        count += 1
print(count*2)