import time
graf = dict()

m = int(input())

stp = time.time()
for i in range(m):
    u, v = input().split()
    if u == v:
        if int(u) not in graf:
            graf[int(u)] = []
    if int(v) in graf:
        graf[int(v)].append(int(u))
    else:
        graf[int(v)] = [int(u)]
    if int(u) in graf:
        graf[int(u)].append(int(v))
    else:
        graf[int(u)] = [int(v)]

virus = list()
ver = sorted(graf.keys(), key=lambda x: len(graf[x]))
for i in ver:
    if len(graf[i]) <= 1:
        virus.append(i)
        continue
    a = set(virus)
    b = set(graf[i])
    ver = list(a & b)
    if len(ver) < 2:
        virus.append(i)
virus_2 = sorted(virus, key=lambda x: len(graf[x]))
for i in virus_2:
    a = set(virus)
    b = set(graf[i])
    ver = list(a & b)
    if len(ver) >= 2:
        virus_2.remove(i)
st1 = time.time()
print(len(virus_2))
print(', '.join([str(i) for i in virus_2]))
print(st1 - stp)
