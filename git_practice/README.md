# Git 연습
git으로 SSAFY 컴퓨터와 집 컴퓨터 동기화 하기



# Git ignore
git이 파일을 추적하지 못하게할때

.gitignore 파일생성 후 파일명을 적는다


```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# celery beat schedule file
celerybeat-schedule

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/
```


# Git branch

- 보기
    - `git branch` : 모든 branch를 보여준다.
- 생성
    - `git branch [브랜치 이름]`: 새 branch 생성
- 이동 (브랜치 간 이동, 커밋 간 이동)
    - `git checkout [브랜치 이름]`: 해당 브랜치로 이동
- 병합
    - `git merge [브랜치 이름]`: 해당 브랜치와 병합


# requests의 GET, POST
- GET: 정보를 가져올 때
- POST: 정보를 입력, 게시할 때
    - 요청(POST)
        - 헤더(요청자의 정보)
        - 번역할 데이터에 대한 정보

# 환경변수 설정으로 API key 숨기기 in python

``` shell
export TWITTER_API_KEY=yoursecretapikey
```


``` python
import os

# twitter_key = os.environ.get('TWITTER_API_KEY')
twitter_key = os.getenv('TWITTER_API_KEY')
```




# 190102

리눅스에서 .파일명    .의 의미는 숨김파일



코드파일 생성한 후 배쉬에서

source 파일명

통해 코드 입힘 





변수명으로 사용불가

```
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```



데이터 사이언스

- 스크래치
- cs50
- Udacity



파이썬

- edx.org
- mitx



파이썬 코드 시각화 툴

python tutor