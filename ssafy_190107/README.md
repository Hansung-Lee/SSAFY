# 파이썬 기초 문법

### 인코딩 선언

인코딩은 선언하지 않더라도 `UTF-8`로 기본 설정이 되어 있다.  
만약, 인코딩을 설정하려면 코드 상단에 아래와 같이 선언한다. 주석으로 보이지만, Python `parser`에 의해 읽혀진다.  

```python
# -*- coding: <encoding-name> -*- 
```

## 변수(variable) 및 자료형

- 같은 값을 동시에 할당할 수 있다.

```python
# 같은 값을 동시에 할당해봅시다.

x = y= 1004

print(id(x))
print(id(y))

x = 2000

print(y)

print(id(x))
print(id(y))


x,y = y,x

print(id(x))
print(id(y))
```
2116516807792  
2116516807792  
1004  
2116516808688  
2116516807792  
2116516807792  
2116516808688  





### String interpolation

1) `%-formatting`  

2) [`str.format()`](https://pyformat.info/)  

3) [`f-strings`](https://www.python.org/dev/peps/pep-0498/) : 파이썬 3.6 버전 이후에 지원 되는 사항입니다.  



```python
# name 변수에 이름을 입력해봅시다.
name = "lim"
```

```python
# %-formatting을 활용해봅시다.
print('hello, %s' % 'asdsad')
print('hello, %d' % 5)
```
hello, asdsad  
hello, 5  


```python
# str.format()을 활용해봅시다.
print('hello, {}'.format(name))
```
hello, lim  

```python
# f-string을 활용해봅시다.
print(f'hello, {name}')
```
hello, lim  



```
a = bool(1)

print("""
asdfsa
asfdsf
asdfsdfdsfs
dfsfds.
{a}!
""")

print(f"""
asdfsa
asfdsf
asdfsdfdsfs
dfsfds.
{a}!
""")
```
asdfsa  
asfdsf  
asdfsdfdsfs  
dfsfds.  
{a}!  

asdfsa  
asfdsf  
asdfsdfdsfs  
dfsfds.  
True!  



### 이스케이프 문자열

문자열을 활용하는 경우 특수문자 혹은 조작을 하기 위하여 사용되는 것으로 `\`를 활용하여 이를 구분한다.

| 예약문자 | 내용(의미)      |
| -------- | --------------- |
| \n       | 줄바꿈          |
| \t       | 탭              |
| \r       | 캐리지리턴      |
| \0       | 널(Null)        |
| `\\`     | `\`             |
| '        | 단일인용부호(') |
| "        | 이중인용부호(") |



## 산술 연산자

Python에서는 기본적인 사칙연산이 가능합니다.

| 연산자 | 내용           |
| ------ | -------------- |
| +      | 덧셈           |
| -      | 뺄셈           |
| *      | 곱셈           |
| /      | 나눗셈         |
| //     | 몫             |
| %      | 나머지(modulo) |
| **     | 거듭제곱       |



## 비교 연산자

우리가 수학에서 배운 연산자와 동일하게 값을 비교할 수 있습니다.

| 연산자 | 내용     |
| ------ | -------- |
| a > b  | 초과     |
| a < b  | 미만     |
| a >= b | 이상     |
| a <= b | 이하     |
| a == b | 같음     |
| a != b | 같지않음 |



## 논리 연산자

| 연산자  | 내용                         |
| ------- | ---------------------------- |
| a and b | a와 b 모두 True시만 True     |
| a or b  | a 와 b 모두 False시만 False  |
| not a   | True -> False, False -> True |



## 연산자 우선순위

1. `()`을 통한 grouping  
2. Slicing  
3. Indexing  
4. 제곱연산자 **  
5. 단항연산자 +, - (음수/양수 부호)  
6. 산술연산자 *, /, %  
7. 산술연산자 +, -  
8. 비교연산자, `in`, `is`  
9. `not`  
10. `and`  
11. `or`   