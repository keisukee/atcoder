# 11 から NN の番号がついた NN 個の荷物と、11 から MM の番号がついた MM 個の箱があります。

# 荷物 ii の大きさは WiWi で、価値は ViVi です。

# 箱 ii には大きさが XiXi 以下の荷物を入れることができます。11 つの箱に 22 つ以上の荷物を入れることはできません。

# QQ 個のクエリが与えられます。各クエリでは 22 つの整数 L,RL,R が与えられるので、次の問題を解いてください。

# - 問題： 個の箱のうち、箱  の  個の箱が使えなくなってしまいました。 残りの箱の中に同時に入れることができる荷物の価値の合計の最大値を求めてください。

#     MM

#     L,L+1,…,RL,L+1,…,R

#     R−L+1R−L+1

N, M, Q = list(map(int, input().split()))
goods = []
for i in range(N):
    w, v = list(map(int, input().split()))
    goods.append([w, v])

goods.sort(key = lambda x: (-x[1], x[0]))
boxes = list(map(int, input().split()))
boxesWithIndex = list(map(lambda i: [boxes[i], i], range(len(boxes))))
boxesWithIndex.sort(key = lambda x: x[0])

queries = []
for i in range(Q):
    left, right = list(map(int, input().split()))
    queries.append([left, right])

# print('goods', goods)
# print('boxes', boxes)
# print('queries', queries)

def getMaxValue(cap, goods):
    for i in range(len(goods)):
        item = goods[i]
        w, v = item
        if w > cap:
            continue
        else:
            goods.remove(item)
            # print('value is', v)
            # print('goods', goods)
            return v
    return 0

def getResult(l, r, boxesWithIndex, goods):
    total = 0
    for i in range(len(boxesWithIndex)):
        cap, boxIdx = boxesWithIndex[i]
        if l-1 <= boxIdx <= r-1:
            # print('skip')
            continue
        else:
            # print('original goods', goods)
            total += getMaxValue(cap, goods)
            # print('value', value)
    return total

for query in queries:
    l, r = query
    # print('==========')
    total = getResult(l, r, boxesWithIndex, goods[:])
    print(total)
    # print('==========')
