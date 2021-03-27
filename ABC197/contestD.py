import math
N = int(input())
x_0, y_0 = list(map(int, input().split()))
x_N2, y_N2 = list(map(int, input().split()))

centerX = (x_0 + x_N2) / 2
centerY = (y_0 + y_N2) / 2

xo_0, y_o0 = (x_0-centerX), (y_0-centerY)

# print('centerX', centerX)
# print('centerY', centerY)
# print('xo_0', xo_0)
# print('y_o0', y_o0)
angle = 360/N
radian = math.radians(angle)
x_1 = (xo_0 * math.cos(radian)) - (y_o0 * math.sin(radian)) + centerX
y_1 = (xo_0 * math.sin(radian)) + (y_o0 * math.cos(radian)) + centerY

print(x_1)
print(y_1)
# print('x_1', x_1)
# print('y_1', y_1)


