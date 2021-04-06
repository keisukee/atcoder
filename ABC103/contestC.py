N = int(input())
sequences = list(map(int, input().split()))

oddSequenceCounter = {}
evenSequenceCounter = {}
for i in range(0, len(sequences), 2):
    even = i
    odd = i+1
    evenNum = sequences[even]
    oddNum = sequences[odd]

    if evenNum not in evenSequenceCounter:
        evenSequenceCounter[evenNum] = 0
    evenSequenceCounter[evenNum] += 1

    if oddNum not in oddSequenceCounter:
        oddSequenceCounter[oddNum] = 0
    oddSequenceCounter[oddNum] += 1

oddNums = list(oddSequenceCounter.items())
oddNums.sort(key = lambda x: -x[1])
evenNums = list(evenSequenceCounter.items())
evenNums.sort(key = lambda x: -x[1])

mostFrequentOddNum, mostFrequentOddNumCount = oddNums[0]
mostFrequentEvenNum, mostFrequentEvenNumCount = evenNums[0]

length = N // 2
if mostFrequentOddNum != mostFrequentEvenNum:
    totalChange = (length-mostFrequentOddNumCount) + (length-mostFrequentEvenNumCount)
    print(totalChange)
else:
    odd1, odd2, even1, even2 = 0, 0, 0, 0
    _, odd1 = oddNums[0]
    _, even1 = evenNums[0]
    if len(oddNums) >= 2:
        _, odd2 = oddNums[1]
    if len(evenNums) >= 2:
        _, even2 = evenNums[1]

    totalChange = min((length-odd1 + length-even2), (length-odd2 + length-even1))
    print(totalChange)
