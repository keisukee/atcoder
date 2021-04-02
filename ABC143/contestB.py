N = int(input())
options = list(map(int, input().split()))

def getAllPairs(options, remain, currentIdx, sumOfPairs, pair):
    if remain == 0:
        sumOfPairs.append(pair[0]*options[currentIdx])
        return

    pair.append(options[currentIdx])
    for i in range(currentIdx+1, len(options)):
        getAllPairs(options, remain-1, i, sumOfPairs, pair)
    pair.pop()
    return


answer = 0
for i in range(len(options)):
    sumOfPairs = []
    getAllPairs(options, 1, i, sumOfPairs, [])
    answer += sum(sumOfPairs)

print(answer)
