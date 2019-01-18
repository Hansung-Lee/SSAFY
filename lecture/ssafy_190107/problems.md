### 문제1

> 다음 과목별 평균 점수를 구하세요. (국어:80 영어:90, 수학:100)

``` python
#여기에 코드를 작성하세요.
score = {
    '국어': 80,
    '영어': 90,
    '수학': 100
}

sum1 = 0

for sc in score:
    sum1 += score[sc]

avg = sum1/len(score)

print (int(avg))
```



### 문제2

> 주어진 리스트의 자연수들이 각각 홀수인지 짝수인지 판별하는 코드를 작성하세요. numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

``` python
#여기에 코드를 작성하세요.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
oddeven = []

for i in numbers:
    if (i%2==1):
        oddeven.append('홀수')
    else:
        oddeven.append('짝수')
print (oddeven)
```





### 문제3

> 1부터 1000까지의 자연수 중 5의 배수에 해당되는 자연수들의 총합을 구하는 코드를 작성하세요.

``` python
#여기에 코드를 작성하세요1

sum2 = 0

for i in range(1,1001):
    if(i%5==0):
        sum2+=i

print(sum2)
```



### 문제4

> for와 range 함수를 이용하여 2~9단까지 구구단을 출력하는 코드를 작성하세요.

``` python
#여기에 코드를 작성하세요.
for i in range(2,10):
    print(f'구구단 {i}단')
    for j in range(1,10):
        print(f"{i} * {j} = {i*j}")
    print('')
```



### 문제5

> 1부터 100까지 자연수를 각각 제곱해 더한 값인 '제곱의 합'과 1부터 100을 먼저 더한 다음에 그 결과를 제곱한 '합의 제곱'의 차이를 구하는 코드를 작성하세요.

``` python
#여기에 코드를 작성하세요.

sum1 = 0  # 제곱의 합
sum2 = 0  # 합의 제곱
result = 0  # 제곱의 합 - 합의 제곱

for i in range(1,101):
    sum1 += i**2
    sum2 += i
    
result = sum1 - (sum2**2)

print (result)
```



## 모음 제거하기

> 다음 문장의 모음을 제거하여 출력하세요.

------

```
예시 입력)
"Life is too short, you need python"
예시 출력)
Lf s t shrt, y nd pythn
```


```python
a = input()
# 아래에 코드를 작성하세요.

li = []
mo = ['a','e','i','o','u']

for i in a:
    if (i in mo):
        continue
    else:
        li.append(i)

for j in li:
    print(j,end="")

```



## 영어 이름 출력하기

> 영어 이름은 가운데 이름을 가지고 있는 경우가 있습니다.
>
> 가운데 이름은 축약해서 나타내는 함수를 작성해보세요.

------

```
예시 입력)
Alice Betty Catherine Davis
예시 출력)
Alice B. C. Davis
```


``` python
name = input()
# 아래에 코드를 작성하세요.

li_name = name.split(' ')
new_name = []
cnt=0

for n in li_name:
	if(cnt==0 or cnt==len(li_name)-1):
    	new_name.append(n)
        cnt+=1
    else:
        new_name.append(n[0]+".")
        cnt+=1
        
for j in new_name:
    print(j,end=" ")
```




## 달력 출력하기

> 1월 1일 월요일부터 12월 31일까지 달력을 출력하세요.


``` python
import calendar

for i in range(1,13):

    print(f'         {i} 월')
    print(calendar.weekheader(2))
    
    k = calendar.monthcalendar(2007,i)


    for j in k:
        for s in j:
            if (s==0):
                print('  ',end=" ")
            elif(int(s)<10):
                print(f'0{s}', end=" ")
            else:
                print(s,end=" ")
        print('')
    print('')
```
