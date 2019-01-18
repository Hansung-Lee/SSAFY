## Intro&Control_of_flow-문제2


### 문제1

> 아래 코드의 출력 결과를 예상해보세요.

``` python
if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")
```
```
3
5
```



### 문제2

> 투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이 투자 경고 종목이라면 '투자 경고 종목입니다'를 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하세요.  

> warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

``` python
#여기에 코드를 작성하세요.

warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
warning = True

while (warning):
    msg = input("투자 하실 종목을 입력하세요.\n")
    if msg in warn_investment_list:
        print('투자 경고 종목입니다.')
        warning = False
    else:
        print('투자 경고 종목이 아닙니다.')
```





### 문제3

> 다음 코드의 결과값을 예측해보세요.

``` python
a = "Life is too short, you need python"

if 'wife' in a:
    print('wife')
elif 'python' in a and 'you' not in a:
    print('python')
elif 'shirt' not in a:
    print('shirt')
elif 'need' in a:
    print('need')
else:
    print('none')
```
```
shirt
```


### 문제4

> 다음 리스트에서 10 이상인 수를 전부 더해서 출력하세요.

> exNumber = [43, 2, 6, 34, 12, 32, 7, 9, 81, 51]

``` python
#여기에 코드를 작성하세요.

exNumber = [43, 2, 6, 34, 12, 32, 7, 9, 81, 51]

sum1 = 0

for num in exNumber:
    if (num>=10):
        sum1 += num
        
print(sum1)

```



### 문제5

> A 기업의 입사 시험은 필기 시험 점수가 80점 이상이면서 코딩 시험을 통과해야 합격이라고 정했습니다. (코딩 시험 통과 여부는 True, False로 구분) 사용자로부터 필기시험 점수를 입력받아 '합격' 혹은 '불합격' 여부를 판단하는 코드를 작성하세요.

``` python
#여기에 코드를 작성하세요.

passorfail = False

score = int(input("입사 시험 점수를 입력하세요.\n"))

if (score >= 80):
    passorfail = True
    
if(passorfail):
    print('합격')
else:
    print('불합격')

```


## Intro&Control_of_flow-문제3


### 문제1

> 다음 소스 코드를 완성하여 1부터 100까지의 숫자를 출력하면서 2의 배수일 때는 'Fizz', 11의 배수일 때는 'Buzz', 2와 11의 공배수일 때는 'FizzBuzz'가 출력되게 만드세요.

``` python
#여기에 코드를 작성하세요.

for i in range(1,101):
    if(i%2==0 and i%11==0):
        print('FizzBuzz')
    elif (i%2==0):
        print('Fizz')
    elif(i%11==0):
        print('Buzz')
    else:
        print(i)

```



### 문제2

> 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하세요.

``` python
#여기에 코드를 작성하세요.
a, b, c = map(int, input("세 개의 숫자를 입력하세요. ex) 20 12 32\n").split())

print ("가장 큰 수: {}".format(max(a,b,c)))
```





### 문제3

> 다음은 학생들의 혈액형(A, B, AB, O)에 대한 데이터입니다. 각 혈액형 별 학생수의 합계를 구하세요.

> blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

``` python
#여기에 코드를 작성하세요.
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

check_blood = [0,0,0,0] # 순서대로 A, B, O, AB

for bt in blood_types:
    if (bt == 'A'):
        check_blood[0]+=1
    elif(bt == 'B'):
        check_blood[1]+=1
    elif(bt == 'O'):
        check_blood[2]+=1
    elif(bt == 'AB'):
        check_blood[3]+=1
    
print (f"""
A형인 학생수의 합계 : {check_blood[0]}
B형인 학생수의 합계 : {check_blood[1]}
O형인 학생수의 합계 : {check_blood[2]}
AB형인 학생수의 합계 : {check_blood[3]}
""")


result = {
    'A': blood_types.count('A'),
    'B': blood_types.count('B'),
    'O': blood_types.count('O'),
    'AB': blood_types.count('AB'),
}

print (result)
```


### 문제4

>다음 리스트의 요소값 중에서 중복되는 값만 뽑아서 새로운 리스트로 옮기고 요소의 개수를 출력하세요. 

>some_lists = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

``` python
#여기에 코드를 작성하세요.

some_lists = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

new_lists = []

for sl in some_lists:
    if (some_lists.count(sl)>1):
        new_lists.append(sl)
        
print(f"중복되는 요소의 개수: {len(set(new_lists))}")

```



### 문제5

>표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다. 네 과목의 평균 점수가 80점 이상일 때 합격이라고 정했습니다. 평균 점수에 따라 '합격', '불합격'을 출력하는 프로그램을 만드세요. 
단, 점수는 0점부터 100점까지만 입력받을 수 있으며 범위를 벗어났다면 '잘못된 점수'를 출력하고 합격, 불합격 여부는 출력하지 않아야 합니다. 

``` python
#여기에 코드를 작성하세요.

korean = int(input("국어 점수를 입력하세요."))
english = int(input("영어 점수를 입력하세요."))
math = int(input("수학 점수를 입력하세요."))
science = int(input("과학 점수를 입력하세요."))

if(0>korean or 0>english or 0>math or 0>science or korean>100 or english>100 or math>100 or science>100):
    print('잘못된 점수')

else:
    sum1 = korean + english + math + science
    avg1 = sum1/4
    
    if(avg1>=80):
        print('합격') 
    else:
        print('불합격')


```


## Intro&Control_of_flow-문제4


### 문제1

>문자열 요소로만 이루어진 리스트에서 문자열 길이가 2 이상이고 주어진 문자열의 첫번째와 마지막 문자가 같은 요소를 모아 새로운 리스트를 만들고 해당 리스트 요소의 개수를 구하세요.

>samples = ['level', 'asdwe', 's', 'abceda', 'gsdwrtfg'] -> 결과값: 3 

``` python
#여기에 코드를 작성하세요.

samples = ['level', 'asdwe', 's', 'abceda', 'gsdwrtfg']

result = []

for sp in samples:
    if (len(sp)>=2):
        if(sp[0]==sp[len(sp)-1]):
            result.append(sp)
            
print(len(result))
```




### 문제2

>다음 리스트에서 중복된 요소를 제거한 리스트를 출력하세요. 

>items = [10,20,40,20,10,30,50,60,40,80,50,40,20,30,10] 

``` python
#여기에 코드를 작성하세요.

items = [10,20,40,20,10,30,50,60,40,80,50,40,20,30,10]

print(list(set(items)))
```





### 문제3

>다음 리스트에서 0번째 4번째 5번째 요소를 지운 새로운 리스트를 생성하세요.

>colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']

``` python
#여기에 코드를 작성하세요

colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']

new_colors = []
deleteindex = [0, 4, 5]

for i in range(len(colors)):
    if (i in deleteindex):
        continue
    else:
        new_colors.append(colors[i])
        
print(new_colors)
```



### 문제4

> 세 정수 A, B, C가 입력값으로 주어질 때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하세요. 

``` python
#여기에 코드를 작성하세요.

A, B, C = map(int, input("세 정수를 입력하세요. ex) 20 12 32\n").split())

li = [A, B, C]

for i in li:
    if i==max(li) or i==min(li):
        continue
    else:
        print(f"두 번째로 큰 정수: {i}")
```



### 문제5

>사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하세요. 각 통화별 환율은 다음과 같습니다. (사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정합니다.)

``` python
#여기에 코드를 작성하세요.

currency = {
    'USD': 1167, 'JPY': 1.096, 'EURO': 1268, 'CNY': 171
}

msg = list(map(str,input("각 통화별 금액을 입력해주세요. ex) 100 달러, 1000 엔, 13 유로, 100 위안\n").split(', ')))

dollar = int(msg[0].split()[0])*currency.get('USD')
en = int(msg[1].split()[0])*currency.get('JPY')
euro = int(msg[2].split()[0])*currency.get('EURO')
wian = int(msg[3].split()[0])*currency.get('CNY')


print(f"""
{msg[0]} = {dollar} 원
{msg[1]} = {en} 원
{msg[2]} = {euro} 원
{msg[3]} = {wian} 원
""")
```
