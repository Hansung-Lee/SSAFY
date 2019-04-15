# Homework_27

1. 로그인을 한 사용자만 게시물을 작성할 수 있도록 코드를 작성하려고한다. 빈칸에 들어갈 코드를 작성하세요.

![image](https://user-images.githubusercontent.com/30791915/56103165-69f0b480-5f6c-11e9-9d50-46c1078a90f6.png)

``` python
class PostCreate(LoginRequiredMixin, CreateView):
	model = Post
	fields = '__all__'
```


2. Question 모델에 게시물을 작성한 사람을 저장할 칼럼을 추가하려고 한다. ForeignKey() 에 넣어야할 인자를 작성하세요.

![image](https://user-images.githubusercontent.com/30791915/56103160-5f361f80-5f6c-11e9-82d2-1c2a6ac98784.png)

``` python
from django.contrib.auth.models import User

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
```
