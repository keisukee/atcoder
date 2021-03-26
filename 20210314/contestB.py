N = int(input())
nums = list(map(int, input().split()))

nodes = {}

for i in range(1, len(nums)+1):
    val = nums[i-1]
    if i not in nodes:
        nodes[i] = []
    nodes[i].append(val)

usableNodes = 0
print('nodes', nodes)

def isNodeInCycle(visited, node, nodes, currentlyInStack):
    visited[node] = True
    currentlyInStack[node] = True

    nodesToSearch = nodes[node]
    for nextnode in nodesToSearch:
        if not visited[node]:
            containesCycle = isNodeInCycle(visited, nextnode, nodes)
            if containesCycle:
                return True
        elif currentlyInStack[node]:
            return True

    currentlyInStack[node] = False
    return False

visited = {i: False for i in range(1, len(nums)+1)}
print('nodes', nodes)
for nextnode in nodes.keys():
    currentlyInStack = {i: False for i in range(1, len(nums)+1)}
    print('currentlyInStack', currentlyInStack)
    print('visited', visited)
    print('nextnode', nextnode)
    print('visited[nextnode]', visited[nextnode])
    if visited[nextnode]:
        print('continue')
        continue
    if isNodeInCycle(visited, nextnode, nodes, currentlyInStack):
        print('cycle', nextnode)
        usableNodes += 1

print('usableNodes', usableNodes)
ans = 2**usableNodes-1

# print('ans', ans)

print('ans', ans)


