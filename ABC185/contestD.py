import math
N, M = list(map(int, input().split()))
stops = list(map(int, input().split()))

stops.sort()
stops = [0] + stops + [N+1]
min_range = N
zones = []
# print(stops)
for i in range(1, len(stops)):
    length = stops[i] - stops[i-1] - 1
    zones.append([stops[i-1] + 1, stops[i]])
    if length > 0:
        min_range = min(min_range, length)

# print(zones)
# print(min_range)

def count_stamp(zones, length):
    total_count = 0
    for zone in zones:
        start, end = zone
        # print('zone', zone)
        # print(math.ceil((end - start) / length))
        total_count += math.ceil((end - start) / length)
    return total_count

total_count = count_stamp(zones, min_range)
print(total_count)
