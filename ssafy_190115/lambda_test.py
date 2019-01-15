import hof
import math

def add_two(num):
    return num+2

print(hof.my_map1(add_two, [1,2,3,4]))

# print(hof.my_map1(lambda 입력 : 출력, [1,2,3,4]))
print(hof.my_map1(lambda num : num+2, [1,2,3,4]))

add_two2 = lambda num : num+2

print(hof.my_map1(add_two2, [1,2,3,4]))


# 1. square 라는 변수에 lambda를 통해 제곱하는 함수를 할당
# 2. cube 라는 변수에 세제곱
# 3. sqrt 변수에 제곱근 (math 활용)

square = lambda num : num**2
cube = lambda num : num**3
sqrt = lambda num : round(math.sqrt(num),2)

print(square(2))
print(cube(2))
print(sqrt(2))

print(hof.my_map1(square, [1,2,3,4]))
print(hof.my_map1(cube, [1,2,3,4]))
print(hof.my_map1(sqrt, [1,2,3,4]))