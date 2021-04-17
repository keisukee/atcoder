K = int(input())

sequences = [0] * K
sequences[0] = 7 % K
for i in range(1, len(sequences)):
    sequences[i] = (sequences[i-1] * 10 + 7) % K

answer = -1
for idx, num in enumerate(sequences):
    if num == 0:
        answer = idx + 1
        break

print(answer)

