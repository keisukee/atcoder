N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

satisfaction = 0
for i in range(len(A)):
    dishId = A[i]
    satisfaction += B[dishId-1]
    if i >= 1 and A[i] - A[i-1] == 1:
        prevDishId = A[i-1]
        satisfaction += C[prevDishId-1]

print(satisfaction)



