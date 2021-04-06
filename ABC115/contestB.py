N = int(input())
prices = []
for i in range(N):
    data = int(input())
    prices.append(data)

maxPrice = max(prices)

totalPrice = sum(prices) - maxPrice // 2
print(totalPrice)