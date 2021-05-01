N, D, H = list(map(int, input().split()))
tilt = H / D
max_fragment = 0
for i in range(N):
    d, h = list(map(int, input().split()))
    t =  (H - h) / (D - d)
    fragment = t * (-d) + h
    max_fragment = max(max_fragment, fragment)

print(max_fragment)