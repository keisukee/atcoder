string = input()
answer = 0
def getAllPossibleFormula(numString, idx, numsToAdd):
    global answer
    if idx == len(numString):
        answer += sum(numsToAdd)
        return

    if numString[idx] == '0':
        getAllPossibleFormula(numString, idx+1, numsToAdd)
    else:
        for i in range(idx, len(numString)):
            currentNum = int(numString[idx : i+1])
            numsToAdd.append(currentNum)
            getAllPossibleFormula(numString, i+1, numsToAdd)
            numsToAdd.pop()
    return

getAllPossibleFormula(string, 0, [])
print(answer)

