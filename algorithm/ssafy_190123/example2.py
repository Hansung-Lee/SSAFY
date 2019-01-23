li = [-3, 3, -9, 6, 7 ,-6, 1, 5, 4, -2]

n = len(li)
cnt = 0

for i in range(1<<n):
    result = 0
    for j in range(n):
        if i & (1<<j):
            result += li[j]
    if result == 0:
        cnt += 1

print(cnt-1)
