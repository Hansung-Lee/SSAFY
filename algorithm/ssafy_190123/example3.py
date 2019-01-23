li = [[9, 20, 2, 18, 11],
      [19, 1, 25, 3, 21],
      [8, 24, 10, 17, 7],
      [15, 4, 16, 5, 6],
      [12, 13, 22, 23, 14]]

li_full = []

for i in li:
    for j in i:
        li_full.append(j)

for i in range(len(li_full)-1):
    min = i
    for j in range(i+1, len(li_full)):
        if li_full[min] > li_full[j]:
            min = j
    li_full[i], li_full[min] = li_full[min], li_full[i]

result = []
for x in range(len(li)):
    result.append([0 for x in range(len(li))])

limit = len(li)
cnt = limit
now_dr = 0   # 0 = right, 1 = down, 2 = left, 3 = up
num = 0

def change_dr(a):
    global limit
    if a%2:
        a += 1
    else:
        limit -= 1
        a += 1
    if a==4:
        a=0
    return a

i = 0
j = 0

for num in li_full:
    result[i][j] = num
    cnt -=1

    if cnt==0:
        now_dr = change_dr(now_dr)
        cnt = limit

    if now_dr == 0:
        j+=1
    elif now_dr == 1:
        i+=1
    elif now_dr == 2:
        j-=1
    elif now_dr == 3:
        i-=1

print(result)


