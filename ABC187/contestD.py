N = int(input())
people = []
enemies = []
allies = []
for i in range(N):
    a, b = list(map(int, input().split()))
    enemies.append(a)
    allies.append(b)
    people.append([a, b])

people.sort(key = lambda x: -(2 * x[0] + x[1]))
# print(people)

enemy_count = sum(enemies)
current_sum = 0
for i in range(len(people)):
    current_sum += sum(people[i])
    enemy_count -= people[i][0]
    if current_sum > enemy_count:
        # print(current_sum)
        print(i+1)
        break
