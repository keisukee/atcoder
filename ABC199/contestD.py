N, M = list(map(int, input().split()))
graph = [[] for i in range(N)]
patterns = {}

for i in range(M):
    a, b = list(map(int, input().split()))
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

total_count = 0

def count_color_pattern(graph, current_edge, patterns):
    global total_count
    # print('current_edge', current_edge)
    # print('patterns', patterns, graph)
    if len(graph) == len(patterns):
        total_count += 1
        return
    if current_edge in patterns:
        return

    choices = ['R', 'G', 'B']
    # choices = [0, 1, 2]
    for edge in graph[current_edge]:
        if edge in patterns:
            # print('patterns[edge]', patterns[edge])
            choices.remove(patterns[edge])
    # print('choices, current_edge', choices, current_edge)
    if len(choices) == 0:
        return

    # print('choices', choices)
    for choice in choices:
        patterns[current_edge] = choice # 0, 1, 2
        # print('choice', choice)
        for edge in graph[current_edge]:
            # print('edge', edge)
            count_color_pattern(graph, edge, patterns)

        del patterns[current_edge]

    return

count_color_pattern(graph, 0, patterns)
print(total_count)