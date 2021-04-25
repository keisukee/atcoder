N = int(input())
string = list(input())
first, second = string[:N], string[N:]
Q = int(input())


def swap(first, second, one, two, N):
    if one < N and two < N:
        first[one], first[two] = first[two], first[one]
    elif one >= N and two >= N:
        one -= N
        two -= N
        second[one], second[two] = second[two], second[one]
    else:
        # print('[before] one, two', one, two)
        if one > two:
            one, two = two, one
        two -= N
        # print('[after] one, two', one, two)
        first[one], second[two] = second[two], first[one]


for i in range(Q):
    t, a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    if t == 1:
        swap(first, second, a, b, N)
    elif t == 2:
        first, second = second, first

transformed_string = ''.join(first + second)
print(transformed_string)