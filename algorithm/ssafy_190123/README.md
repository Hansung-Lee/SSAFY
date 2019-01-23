## 2차원 배열 알고리즘

### 지그재그 순회
``` python
for i in range(len(list)):
	for j in range(len(list[0])):
		list[i][j + ((m-1-2*j)*(i%2))]
```

### 전치 행렬
``` python
for i in range(3):
	for j in range(3):
		if i < j:
			list[i][j], list[j][i] = list[j][i], list[i][j]
```

## 부분집합의 합

### 비트 연산자
```python
li = [1,2,3]

n = len(li)

for i in range(1<<n): # 1<<n: 2^n(부분집합의 개수)
    for j in range(n+1): # 원소의 수만큼 비트를 비교함
        if i & (1<<j): # i의 j번째 비트가 1이면 j번째 원소 출력
            print(li[j], end=", ")
    print()
print()

```



## 이진 검색
### 이진 검색 알고리즘
```python
def binarySearch(li, key):
	start = 0
	end = len(li)-1
	while start <= end:
		middle = (start + end)//2
		if li[middle] == key: # 검색 성공
			return True
		elif li[middle] > key:
			end = middle -1
		else:
			start = middle +1
	return False
```

