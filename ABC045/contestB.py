from collections import deque
cards = {}

for char in ['a', 'b', 'c']:
    data = list(input())
    cards[char] = deque(data)

playerCards = cards['a']
while playerCards:
    nextPlayer = playerCards.popleft()
    playerCards = cards[nextPlayer]

print(nextPlayer.upper())


