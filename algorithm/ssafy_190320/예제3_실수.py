msg = input()

pattern = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9
}
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
start = 0

for i in range(len(li)):
    temp = ''.join([str(x) for x in li[i:i+6]])
    if pattern.get(temp) != None:
        start = i
        break

for i in range(start,len(li)-(start+1+len(li)%6),6):
    temp = ''.join([str(x) for x in li[i:i+6]])
    result.append(pattern.get(temp))

print(result)