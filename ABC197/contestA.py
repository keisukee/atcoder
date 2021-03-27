string = input()

s = list(string)
head = s.pop(0)
s.append(head)
print(''.join(s))