from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def lotto(request):
    lucky = random.sample(range(1,46), 6)
    lucky.sort()
    return render(request, 'lotto.html', {'lucky': lucky})
    
def hello(request, name):
    return render(request, 'hello.html', {'name': name})
    
def dinner(request):
    menu = ['한식', '중식', '일식', '양식', '분식']
    result = random.choice(menu)
    return render(request, 'dinner.html', {'result':result})
    
def reverse(request, word):
    rvs_word = word[::-1]
    return render(request, 'reverse.html', {'word': word, 'rvs_word': rvs_word})
    
def sqrt(request, num):
    return render(request, 'sqrt.html', {'num': num, 'result': num**2})