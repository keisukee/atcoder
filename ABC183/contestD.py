N, W = list(map(int, input().split()))
events = []
for i in range(N):
    s, t, p = list(map(int, input().split()))
    events.append([s, p])
    events.append([t, -p])

events.sort(key = lambda x: (x[0], x[1]))

water_supply = 0
can_supply = True
# print(events)
for event in events:
    water_supply += event[1]
    # print(water_supply)
    if water_supply > W:
        can_supply = False
        break

if can_supply:
    print("Yes")
else:
    print("No")


