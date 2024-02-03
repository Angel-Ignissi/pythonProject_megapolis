with open('1.txt') as f:
    s = f.readline()
    li = [s.strip().split('\t') for s in f]
