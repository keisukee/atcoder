N = int(input())
parameters = []
for i in range(N):
    data = list(map(int, input().split()))
    parameters.append(data)

max_power = 0
for i in range(len(parameters)-2):
    a = parameters[i]
    max_power_a = max(a)
    if max_power_a < max_power:
        continue
    for j in range(i+1, len(parameters)-1):
        b = parameters[j]
        max_power_b = max(b)
        if max_power_b < max_power:
            continue
        for k in range(j+1, len(parameters)):
            c = parameters[k]
            team_parameters = [max(a[x], b[x], c[x]) for x in range(len(a))]
            max_power = max(max_power, min(team_parameters))

print(max_power)
