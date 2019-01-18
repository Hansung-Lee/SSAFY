# 자동화할 기능들을 파이썬으로 구현

import webbrowser
import sys

url = 'https://www.google.com/search?q='+''.join(x+' ' for x in sys.argv[1:])
webbrowser.open(url)