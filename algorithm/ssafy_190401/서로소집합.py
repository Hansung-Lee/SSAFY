def make_set(x):
    p[x] = x

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])

    return p[x]

def union(x, y):
    temp = find_set(y)
    for j in range(1, len(p)):
        if p[j] == temp:
            p[j] = find_set(x)


T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    p = [x for x in range(N+1)]

    for i in range(0, len(li), 2):
        union(li[i], li[i+1])
    
    p = list(set(p))

    print("#{} {}".format(t+1, len(p)-1))