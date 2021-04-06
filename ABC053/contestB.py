characters = list(input())

idxA = None
idxZ = None
for idx, char in enumerate(characters):
    # print('idx, char', idx, char)
    if char == 'A' and idxA is None:
        idxA = idx

    if char == 'Z':
        idxZ = idx

print(idxZ-idxA+1)
# print(''.join(characters[idxA : idxZ + 1]))