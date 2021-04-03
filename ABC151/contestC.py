N, M = list(map(int, input().split()))
penalties = [0] * N
hasAnswer = set()
totalPenalty = 0
totalCorrectAnswers = 0
for i in range(M):
    data = input().split()
    question = int(data[0])
    result = data[1]
    # print('result', result)
    if result == 'AC' and question not in hasAnswer:
        hasAnswer.add(question)
        totalCorrectAnswers += 1
        totalPenalty += penalties[question-1]

    if result == 'WA':
        penalties[question-1] += 1

print(totalCorrectAnswers, totalPenalty)


