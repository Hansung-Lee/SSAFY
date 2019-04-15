# Homework_22

1. attachment column에 파일을 저장하려고 한다. 아래의 (a)에 정의 해야 하는 field는?

![image](https://user-images.githubusercontent.com/30791915/56102310-3e1f0000-5f67-11e9-9499-22ba114fa39b.png)


``` python
class Post(models.Model):
	attachment = models.FileField(upload_to=user_directory_path)
```


2. 사용자가 업로드한 파일이 저장되는 위치를 Django 프로젝트 폴더 내부의 '/uploaded_files'로 지정하고자한다. 이 때, settings.py에 작성해야 할 설정 2가지와 이것이 의미하는 바를 간략하게 작성하시오.

``` python
# 각 파일에 대한 URL Prefix
MEDIA_URL = '/uploaded_files/' # 항상 / 로 끝나도록 설정

# 업로드된 파일을 저장할 디렉토리 경로
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
```

3. 개발자가 작성한 CSS 파일이나 넣고자 하는 이미지 파일 등이 Django 프로젝트 폴더 내부의 '/assets'에 있다. '이 폴더 안에 정적 파일이 있다.'라고 Django 프로젝트에게 알려주기 위해서 settings.py에 작성해야하는 설정을 작성하시오.

``` python
STATIC_ROOT = "/assets/"

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
) 
```

