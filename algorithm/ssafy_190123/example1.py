import random

li = [[-1] * 7]

for j in range(5):
    temp_li = [-1]
    for i in range(5):
        temp_li.append(random.randrange(1,51))
    temp_li.append(-1)
    li.append(temp_li)

li.append([-1] * 7)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0 ,0]
num = 0
li_num = []
for x in range(7):
    li_num.append([0 for x in range(7)])

for i in range(1,len(li)-1):
    for j in range(1, len(li[0])-1):
        num = 0
        for z in range(4):
            if li[i+dx[z]][j+dy[z]] == -1:
                continue
            else:
                if li[i][j]>li[i+dx[z]][j+dy[z]]:
                    num += li[i][j] - li[i+dx[z]][j+dy[z]]
                else:
                    num += li[i+dx[z]][j+dy[z]] - li[i][j]
        li_num[i][j] = num


print('--리스트--')
for i in range(1,len(li)-1):
    for j in range(1, len(li[0])-1):
        print(li[i][j], end=' ')
    print('')
print('')
print('---답---')
for i in range(1,len(li_num)-1):
    for j in range(1, len(li_num[0])-1):
        print(li_num[i][j], end=' ')
    print('')