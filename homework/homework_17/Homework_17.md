# Homework_17

1. Django에서 선언한 Model을 실제 DB에 반영하는 과정을 무엇이라고 하는가?

```
migration
```

2. 모델의 필드를 정의할 때 CharField는 필수로 들어가야하는 인자가 존재한다. 무엇인가?

```
max_length (길이 제한)
```

3. Django 에서 동작하는 모든 명령을 대화식 Python 쉘에서 시험할 수 있는 명령어를 작성하세요

```
python manage.py shell
```

4. Post라는 이름의 모델은 CharField로 정해진 title과 CharField로 정해진 content가 필드로 정의 되어있다. 제목은 자신의 이름, 내용은 자신의 이메일 정보가 들어간 Post를 만드는 코드를 작성하세요

``` python
# models.py
from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
```
``` 
> p = Post(name="이름", email="이메일 정보")
> p.save()
```