# Homework_35

1. JS 는 ES6 이전과 이후로 많은 것이 바뀌었다. ES5 까지는 ‘var ‘키워드로 변수를 선언했다면, ES6 이후로는 ‘let’ 과 ‘const’ 키워드가 등장했다. ‘let’ 과 ‘const’ 의 차이점과 언제 사용하는지 간략하게 기술하시오.

```
var는 function-scoped 이고, let,const 는 block-scoped 입니다.
var의 function-scoped라는 뜻은 유효 범위가 함수 단위 라는 뜻이고,
let,const의 block-scoped라는 뜻은 유효 범위가 블록, 즉 {}로 감싸지는 범위라는 뜻입니다.

let과 const
공통점 : 변수 재선언 불가능
차이점 : immutable 여부가 다르다
let의 경우에는 값이 변하는 식별자일 경우 사용, 변수에 재할당이 가능
const의 경우에는 값이 변하지 않는 식별자일 경우 사용, 재할당이 불가능
```

2. JS 에서는 key – value 로 이루어진 자료구조를 Object 라고 부른다. Object와 JSON 의 차이를 간략하게 기술하시오.

```
Object는 **JS Engine 메모리 안에 있는 데이터 구조**이고,
JSON은 **객체의 내용을 기술하기 위한 text 파일**이라는 점이 다릅니다.
JSON은 "파일"이므로 확장자 명이 **.JSON인 파일**이 존재합니다.

1.JSON : 파일포맷 & 단순 문자열(string)
2.javascript object : javascript 코드가 읽을 수 있는 오브젝트
```

3. 해당 코드에서 ‘Value’ 에 접근하는 두 가지 방법(코드)을 모두 작성하시오.

![image](https://user-images.githubusercontent.com/30791915/56946245-8263f000-6b64-11e9-9e3f-ac34d754db93.png)

```
myObject['key'] 또는 myObject.key
```

4. 아래 주석에 따라 JS 코드를 작성하시오.

![image](https://user-images.githubusercontent.com/30791915/56946259-8abc2b00-6b64-11e9-9d54-1ca498ab4862.png)

``` html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
</head>
<body>
    <h1>Hello World!</h1>
    <script>
        // 1. h1 태그를 선택한 뒤, header 라는 상수에 할당한다.
        header = document.querySelector('h1')
        // 2. 브라우저 콘솔에 header 안의 내용을 출력한다.
        console.log(header.innerText)
        // 3. header 안의 내용을 'Happy Hacking!'으로 변경한다.
        header.innerText = 'Happy Hacking!'
    </script>
    
</body>
</html>
```
