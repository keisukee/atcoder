# N = int(input())
# sequences = list(map(int, input().split()))
# monotonousIncreasingCount = 0
# left = 0
# right = 0
# pairs = []
# while right < len(sequences)-1:
#     monotonousIncreasingCount += 1
#     pairs.append((right, right))
#     if sequences[right] >= sequences[right+1]:
#         while left < right:
#             left += 1
#             monotonousIncreasingCount += 1
#             pairs.append((left, right))
#     else:
#         if left != right:
#             monotonousIncreasingCount += 1
#             pairs.append((left, right))
#     right += 1

# print('monotonousIncreasingCount', monotonousIncreasingCount)
# print('pairs', pairs)


N=int(input())
A=list(map(int,input().split()))
diff=0
ans=N
for i in range(N-1):
    if A[i]<A[i+1]:
        diff+=1
        ans+=diff
    else:
        diff=0
print(ans)