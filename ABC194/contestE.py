from collections import deque
N, M = list(map(int, input().split()))
sequences = list(map(int, input().split()))

def get_min_positive(sequences, length):
    queue = deque(sequences[0 : length+1])
    encounted = set(queue)
    min_candidate = min(queue)-1

    for i in range(length, len(sequences)-length+1):
        num = sequences[i]

        queue.append(num)
        encounted.add(num)

        popped_value = queue.popleft()
        del encounted[popped_value]

        if popped_value < 0:
            continue

        if popped_value < min_candidate:
            min_candidate = popped_value


        # value = heapq.heappop(minheap)
        # min_candidate = value - 1
        # encounted.add(value)
        # if min_candidate >= 0 and min_candidate not in encounted:
        #     return min_candidate

        # min_candidate = value

    return min_candidate + 1

min_candidate = float('inf')
# for i in range(N-M+1):
#     get_min_positive(sequences, N)
# print(min_candidate)


