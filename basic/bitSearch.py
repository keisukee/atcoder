item = (("みかん", 100), ("りんご", 200), ("ぶどう", 300), ("すいか", 500))
n = len(item)

for i in range(2**n):
    combo = []
    for j in range(n):
        if (i >> j & 1):
            combo.append(item[j])
    print(combo)

