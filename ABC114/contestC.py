N = int(input())

def dfs(string, N):
    if int(string) > N:
        return 0
    count = 1 if all(c in string for c in list('753')) else 0
    for c in list('753'):
        count += dfs(string + c, N)
    return count

count = dfs('0', N)
print(count)
