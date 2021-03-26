N = int(input())

count = [
    [10**1, 0],
    [10**2, 9],
    [10**3, 0],
    [10**4, 90],
    [10**5, 0],
    [10**6, 900],
    [10**7, 0],
    [10**8, 9000],
    [10**9, 0],
    [10**10, 90000],
    [10**11, 0],
    [10**12, 900000]
]

totalCount = 0
lastIdx = 0

while count[lastIdx][0] <= N:
    totalCount += count[lastIdx][1]
    lastIdx += 1

lastIdx -= 1

def splitHalf(num):
    string = list(str(num))
    mid = len(string) // 2
    half = [int(''.join(string[:mid])), int(''.join(string[mid:]))]
    # print('half', half)
    return half

start = count[lastIdx][0]
# print('start', start)
if len(str(start)) % 2 == 0:
    half = splitHalf(N)
    boundary, _ = splitHalf(start)
    # print('boundary', boundary)
    if half[0] > half[1]:
        # +0
        totalCount += half[0] - boundary
    else:
        # +1
        totalCount += half[0] - boundary + 1
    # print('half', half)

print(totalCount)
