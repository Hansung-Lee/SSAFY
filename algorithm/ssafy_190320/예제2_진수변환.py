msg = input()

li = []

for m in msg:
    temp = ''
    try:
        n = int(m)
    except:
        n = ord(m)-55
    for i in range(4):
        temp += str(n%2)
        n //= 2
    li.extend(list(map(int, temp[::-1])))


result = []

for i in range(0,len(li),7):
    temp = li[i:i+7]
    temp_result = 0
    for j in range(len(temp)):
        temp_result += temp[j]*(1<<(len(temp)-j-1))
    result.append(temp_result)

print(result)