# Homework_26

1. Django Form을 활용하기 위해서 클래스를 만들때 장고 내부에 만들어져있는 클래스를 상속받아서 활용해야 한다. 이 클래스를 import 하는 문장을 작성하세요.

``` python
from django import forms
```


2. 폼 클래스를 템플릿에서 활용하기 위해서 form이라는 이름으로 템플릿 페이지로 전달하였다. 템플릿 페이지에서 form을 <p>태그들로 감싸서 렌더링 하기 위한 코드를 작성하세요.

``` html
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
</form>
```

3. 폼 클래스를 활용할때 폼에 담긴 데이터가 유효한지 체크하기 위해서 is_valid() 메소드를 활용한다. is_valid() 메소드를 통과하고 나서 사용자의 데이터를 가져오기 위해서 빈칸에 들어가야할 코드를 작성하세요.

![image](https://user-images.githubusercontent.com/30791915/56102806-55abb800-5f6a-11e9-9b57-23516db0926f.png)


``` python
def create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_vaild():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
```

