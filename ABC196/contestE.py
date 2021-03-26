N = int(input())
A, T = [], []
for i in range(N):
    a1, t1 = list(map(int, input().split()))
    A.append(a1)
    T.append(t1)

Q_num = int(input())
Q_array = list(map(int, input().split()))

def getFuncResult(t_i, x, a_i):
    if t_i == 1:
        return x + a_i
    elif t_i == 2:
        return max(x, a_i)
    else:
        return min(x, a_i)

for q in range(1, Q_num+1):
    x_i = Q_array[q-1]
    prevVal = None
    for i in range(1, N+1):
        a_i, t_i = A[i-1], T[i-1]
        print('prevVal', prevVal)
        if i == 1:
            prevVal = getFuncResult(t_i, x_i, a_i)
        else:
            prevVal = getFuncResult(t_i, prevVal, a_i)

    print('==============')
    print(prevVal)
