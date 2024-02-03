with open('1.txt') as f:
    s = f.readline()
    li = [s.strip().split('\t') for s in f]
    new_li = []
    li.sort(key=lambda x: [-int(x[0])])
    print(*li[:3])
