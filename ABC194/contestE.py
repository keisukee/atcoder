import collections
N, M = map(int, input().split())
A = list(map(int, input().split()))

bucket = collections.Counter(A[:M])
ans = float('inf')

def mex(bucket):
    for i in range(N+1):
        if bucket[i] == 0:
            return i

ans = min(ans, mex(bucket))
for i in range(N-M):
    bucket[A[i]] -= 1
    bucket[A[M+i]] += 1

    if A[i] < ans and bucket[A[i]] == 0:
        ans = A[i]

print(ans)
