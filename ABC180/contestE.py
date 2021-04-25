
N = int(input())
cities = []

for i in range(N):
    a, b, c, = list(map(int, input().split()))
    cities.append([a, b, c])


def calc_move_cost(one_idx, two_idx, cities):
    x1, y1, z1 = cities[one_idx]
    x2, y2, z2 = cities[two_idx]
    return abs(x2-x1) + abs(y2-y1) + max(0, z2-z1)
print('hoge')