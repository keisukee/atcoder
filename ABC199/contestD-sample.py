n, m = map(int, input().split())
paths = [(i, []) for i in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    paths[a][1].append(b)
    paths[b][1].append(a)
paths.sort(key=lambda path: len(path[1]), reverse=True)  # 繋がっているものが多い順
# print(paths)

color_map = [0 for _ in range(n)]


def counting(index):  # index = 枝の節の位置（上から何番目か）
    if index == n:
        # print("最後まで到達")
        return 1
    pos, path = paths[index]  # position and linked paths
    if len(path) == 0:
        # print("これ以降繋がっていない")
        return 3**(n - index)  # 繋がっていないので個々は3通りある
    flag = [True for _ in range(4)]  # 0,1,2,3で不可と3色を表す
    for node in path:
        flag[color_map[node]] = False  # 使われている色をfalse
    ret = 0
    for color in range(1, 4):
        if flag[color]:  # 使われていない色がある
            color_map[pos] = color
            ret += counting(index+1)
        # 全色使われている時は不可
    color_map[pos] = 0
    # print("無理")
    return ret


if n > 1:
    color_map[paths[0][0]] = 1
    print(counting(1)*3)
else:
    print(3)
