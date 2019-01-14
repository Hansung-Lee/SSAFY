# 두 개의 함수를 정의한다.
# square(num) => num을 제곱 해주는 함수
# cube(num) => num을 세제곱 해주는 함수

def square(num):
    return num**2

def cube(num):
    return num**3

if __name__ == "__main__":
    print(square(2))
    print(cube(2))


# 파일이 직접 실행되면 => "__main__"
# 파일이 불려오게 되면(import) => "파일명"
print(__name__)