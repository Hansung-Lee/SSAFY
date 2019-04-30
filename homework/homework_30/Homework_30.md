# Homework_30


![image](https://user-images.githubusercontent.com/30791915/56945779-3bc1c600-6b63-11e9-8495-da152d39037b.png)

1. Post 모델과 User 모델을 M:N 관계로 설정 하여 좋아요 기능을 구현하려고 한다. 이때 빨간색 박스에 들어갈 클래스의 이름은 무엇인가?

```
ManyToManyField
```

2. 좋아요 기능을 구현하기 위하여 User모델과 M:N 관계설정을 하려고 한다. 그런데 user 칼럼에서 이미 User모델과 관계설정이 되어있기 때문에 이를 구분하기 위해 초록색 박스에 들어갈 옵션은 무엇인가?

```
related_name
```