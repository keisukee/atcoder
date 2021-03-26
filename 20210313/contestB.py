# 問題文
# みかんがたくさんあります。どのみかんの重さも 
# A
#  グラム以上 
# B
#  グラム以下であることがわかっています。（みかんの重さは整数とは限りません。）

# この中からいくつかのみかんを選んだところ、選んだみかんの重さの合計がちょうど 
# W
#  キログラムになりました。

# 選んだみかんの個数として考えられる最小値と最大値を求めてください。ただし、このようなことが起こり得ないなら、かわりにそのことを報告してください。
# A, B, W
# input: 120 150 2
# output: 14 16
# ans = 2000
import math
A, B, W = list(map(int, input().split()))
w_gram = W * 1000

minCount = math.ceil(w_gram/B)
maxCount = math.floor(w_gram/A)
if minCount > maxCount:
    print('UNSATISFIABLE')
else:
    print(minCount, maxCount)



