data = input()
string = 'ZONe'
count = 0
for i in range(len(data)):
    if data[i:i+4] == string:
        count += 1

print(count)