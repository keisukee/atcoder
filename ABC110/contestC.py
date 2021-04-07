from collections import Counter
stringOne = list(input())
stringTwo = list(input())
counterOne = Counter(stringOne)
counterTwo = Counter(stringTwo)

counterOneFrequency = list(counterOne.values())
counterOneFrequency.sort()
counterTwoFrequency = list(counterTwo.values())
counterTwoFrequency.sort()

if counterOneFrequency == counterTwoFrequency:
    print('Yes')
else:
    print('No')
