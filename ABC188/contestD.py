N, C = list(map(int, input().split()))
events = []
for i in range(N):
    a, b, c = list(map(int, input().split()))
    a -= 1
    events.append([a, c])
    events.append([b, -c])

events.sort()
# for event in events:
#     print(event)

total_price = 0
current_day, current_price = 0, 0
for day, price in events:
    if day != current_day:
        total_price += min(C, current_price) * (day - current_day)
        current_day = day
    current_price += price

print(total_price)


