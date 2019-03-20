msg = input()
li = []
for m in msg:
    if m ==' ':
        continue
    else:
        li.append(int(m))

result = []

for i in range(0,len(li),7):
    temp = li[i:i+7]
    temp_result = 0
    for j in range(len(temp)):
        temp_result += temp[j]*(1<<(len(temp)-j-1))
    result.append(temp_result)

print(result)