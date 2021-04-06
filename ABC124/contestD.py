# N, K = list(map(int, input().split()))
# string = list(input())
# isZeroFirst = string[0] == '0'
# continuousCount = []
# count = 1
# for i in range(1, len(string)):
#     if string[i] == string[i-1]:
#         count += 1
#     else:
#         continuousCount.append(i)
#         count = 1


# maxLength = 0
# for i in range(len(continuousCount)):
#     if i + 2*K + 1 >= len(continuousCount):
#         break
#     maxLength = continuousCount[i+2*K+1] - continuousCount[i]

# print(continuousCount)


N, K = list(map(int, input().split()))
S = input()
pre = '1'
l = []
l.append(0)
for i, s in enumerate(S):
    if s != pre:
        l.append(i)
    pre = s
l.append(N)
if S[-1] == '0':
    l.append(N)
print(l)
if len(l) <= 2*K+1:
    print(N)
else:
    ans = 0
    for i in range(0, len(l)-2*K-1, 2):
        ans = max(ans, l[i+2*K+1]-l[i])
    print(ans)