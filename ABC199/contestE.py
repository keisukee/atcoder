N, M = list(map(int, input().split()))
sequence = [i for i in range(1, N+1)]

for i in range(M):
    x, y, z = list(map(int, input().split()))

def create_permutations(sequence, idx):
    if idx == len(sequence):
        print(sequence)
        return

    for i in range(idx, len(sequence)):
        sequence[idx], sequence[i] = sequence[i], sequence[idx]
        create_permutations(sequence, idx+1)
        sequence[idx], sequence[i] = sequence[i], sequence[idx]

    return

create_permutations(sequence, 0)