orders = input()

stack = []
for order in orders:
    if order == '0':
        stack.append('0')
    elif order == '1':
        stack.append('1')
    elif order == 'B':
        if stack: stack.pop()

print(''.join(stack))
