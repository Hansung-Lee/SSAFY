# Homework_32

1. Django에서 모델의 기초 데이터베이스의 값을 제공하기 위해서는 Fixtures를 사용한다. 해당 파일은 기본적으로 각각의 app에 fixtures 폴더에 있어야하며, 파일 형식은 [ ]이거나 [ ]이다.

```
.json 이거나 .yaml 이다.
```

2. 워크샵처럼 실제 Django에 데이터가 저장되어 있을 때, 아래의 fixtures 파일을 만들고자 한다. 사용해야하는 명령어를 작성하라.

![image](https://user-images.githubusercontent.com/30791915/56945905-a70b9800-6b63-11e9-86f5-56d2a5d9a20c.png)

``` shell
python manage.py dumpdata myapp.person < person.yaml
```

