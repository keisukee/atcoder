items = (("みかん", 100), ("りんご", 200), ("ぶどう", 300), ("すいか", 500))
n = len(items)

def permutation(items, currentIdx, combo):
    if currentIdx == len(items):
        print(combo)
        return
    
    
