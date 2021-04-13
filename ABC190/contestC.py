N, M = list(map(int, input().split()))
conditions = []
choices = []
for i in range(M):
    a, b = list(map(int, input().split()))
    conditions.append([a, b])

K = int(input())
for i in range(K):
    c, d = list(map(int, input().split()))
    choices.append([c, d])

def get_meet_requirement_count(conditions, choices):
    max_count = 0
    for i in range(2**len(choices)):
        balls = set()
        for j in range(len(choices)):
            if (i >> j & 1):
                balls.add(choices[j][1])
            else:
                balls.add(choices[j][0])

        current_count = 0
        for condition in conditions:
            if condition[0] in balls and condition[1] in balls:
                current_count += 1
        max_count = max(max_count, current_count)
    return max_count

max_count = get_meet_requirement_count(conditions, choices)
print(max_count)
