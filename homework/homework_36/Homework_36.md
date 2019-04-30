# Homework_36

1. DOM에서 특정 요소를 선택할 때 document.querySelector() 뿐만 아니라 document.querySelectorAll() 역시 사용할 수 있다. 둘의 차이를 검색하여 기술하시오.

```
document.querySelector()는 동일한 클래스명을 가진 객체중 첫번째 것을 반환하고,
document.querySelectorAll()은 해당 선택자에 해당하는 모든 요소를 가져온다.
```

2. JS에서 자주 사용하는 EventListener 들 중 아래와 같은 것들이 있다. 각각 간략하게 어떤 Trigger 를 의미하는지 조사하여 간략하게 기술하시오.

```
- click - 클릭시 발생
- mouserover - 마우스가 특정 객체 위로 올려졌을때
- mouseout - 마우스가 특정 객체 밖으로 나갔을 때 발생
- mousemove - 마우스가 움직였을 때 발생
- keypress - 키를 눌렀을 때 발생(아스키코드 대소문자구별, 문자가 아닌키 불가능)
- keydown - 키를 눌렀을 때 발생(문자키나 기능키 등의 모든키 가능)
- keyup - 키에서 손을 땟을 때 발생
- load - 로드가 완료 되었을 때 발생
- scroll - document view나 element가 스크롤 될 때 발생
- change - 변동이 있을 때 발생
```

3. DOM 에 요소를 추가할 때, innerHTML += 의 방법과 appendChild() 함수를 통해 추가하는 방법이 있다. 둘의 차이를 간략하게 기술하시오.


```
appendChild는 현재 위치에 그냥 추가만 하는 것이고, innerHTML은 전체태그에 합쳐진다는 것이다. innerHTML +=를 사용해서 즉, 계속적으로 전체데이터 + 추가데이터를 새로 쓰는 효과가 된다. appendChild는 추가데이터만 등록하는 효고, 추가 데이터만 필요할 때는 이것을 쓰는 것이 빠르다.
```