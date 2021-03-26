# 問題文
# 高橋君は整数を書くとき、下から 
# 3
#  桁ごとにコンマで区切って書きます。例えば 
# 1234567
#  であれば 1,234,567、
# 777
#  であれば 777 と書きます。

# 高橋君が 
# 1
#  以上 
# N
#  以下の整数を 
# 1
#  度ずつ書くとき、コンマは合計で何回書かれますか？

# 制約
# 1
# ≤
# N
# ≤
# 10
# 15
# N
#  は整数

N = int(input())

def calcComma(N):
    totalCount = 0
    num = 1
    boundary = 1000
    nextBoundary = 1000
    commaPerNum = 0
    while num <= N:
        if num >= boundary:
            print('num, boundary', num, boundary)
            print('num >= boundary', num >= boundary)
            commaPerNum += 1
            boundary *= 1000
        totalCount += commaPerNum
        num += 1

    return totalCount

def calcCommaV2(N):
    if N < 1000:
        return 0

    totalCount = 0
    boundary = 1000
    nextBoundary = boundary * 1000
    commaPerNum = 0
    num = 1000
    while num <= N:
        if num >= boundary and N >= nextBoundary:
            # print('prev: num', num)
            commaPerNum += 1
            totalCount += commaPerNum * (nextBoundary-boundary)
            num = nextBoundary
            # print('after: num', num)
            nextBoundary *= 1000
            boundary *= 1000
        else:
            commaPerNum += 1
            totalCount += commaPerNum * (N-boundary+1)
            num = nextBoundary
            boundary *= 1000
            nextBoundary *= 1000

    return totalCount

# totalCount = calcComma(N)
totalCountV2 = calcCommaV2(N)

# print('totalCount', totalCount)
print(totalCountV2)