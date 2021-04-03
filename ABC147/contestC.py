N = int(input())
statements = []
for i in range(N):
    a_i = int(input())
    data = []
    for j in range(a_i):
        x, y = list(map(int, input().split()))
        data.append((x, y))
    statements.append(data)

def bitSearch(statements, N):
    maxHonestPeople = 0
    for i in range(1 << N):
        print('bin: ', bin(i))
        honest = 0
        isValid = True
        for j in range(N):
            if (i >> j & 1):
                honest += 1
                for state in statements[j]:
                    person, isHonest = state
                    if isHonest:
                        print('honest:', person-1, j & 1 << (person-1))
                        isValid &= j & 1 << (person-1)
                    else:
                        isValid &= (j & 1 << (person-1)) == 0
        if isValid:
            maxHonestPeople = max(maxHonestPeople, honest)
    print('maxHonestPeople', maxHonestPeople)


print('statements', statements)
bitSearch(statements, N)