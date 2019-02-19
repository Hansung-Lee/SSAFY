# Homework_19

1. Django에서는 사용자가 자신의 의지와는 무관하게 공격자가 의도한 행위를 특정 웹 사이트에 요청하게 하는 공격을 막는 기능을 기본적으로 동작시킨다. 위의 공격은 무엇을 의미 하는가?

```
Cross-Site Request Forgery (CSRF)
```

2. 기본적으로 Django에서 views.py에 함수들을 정의할 때 request인자 값을 넣어주어야 한다. request를 활용해서 아래의 폼을 통해서 들어온 데이터를 가져오는 코드를 작성하세요  
![image](https://user-images.githubusercontent.com/30791915/52994771-fa72b300-345b-11e9-85c1-006a81a6c9ec.png)  
``` python
title = request.GET.get('title')
```

3. 다음은 사용자가 이미 작성한 글을 수정하기 위해서 기존의 글을 보여주는 edit페이지를 위한 views.py의 코드이다.  
![image](https://user-images.githubusercontent.com/30791915/52994816-1d04cc00-345c-11e9-8565-f9585193f9b8.png)  

아래의 코드에 기존의 데이터를 보여줄 수 있도록 코드를 수정하세요  
![image](https://user-images.githubusercontent.com/30791915/52994827-2beb7e80-345c-11e9-8f7d-08e95210d787.png)

``` html
<form action="/posts/{{post.id}}/update/" method="POST">
	{% csrf_token %}
	<input type="text" name="title" value={{post.title}}>
	<input type="text" name="content" value={{post.content}}>
	<input type="text" value="submit">
</form>
```
