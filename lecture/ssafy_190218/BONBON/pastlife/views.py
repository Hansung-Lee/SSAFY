from django.shortcuts import render
from .models import Job
from faker import Faker
import os
import requests

# Create your views here.
def index(request):
    return render(request, 'pastlife/index.html')
    
def pastlife(request):
    name = request.GET.get('name')
    fake = Faker('ko-KR')
    job = fake.job()
    
    # 만약 해당 이름이 DB에 저장되어 있다면,
    #   DB에 저장된 값을 가져온다.
    # 없다면,
    #   faker를 통해 fake 정보를 만들어
    #   DB에 추가하고 해당 값을 job에 저장한다.
    
    # filter는 None, get은 에러
    person = Job.objects.filter(name=name).first()
    # person = Job.objects.get(name=name)

    if person:
        job = person.job
        result = {
            'name': name,
            'job': job
        }
    else:
        result = {
            'name': name,
            'job': job,
        }
        # person = Job(name=name, job=job)
        # person.save()
        Job.objects.create(name=name, job=job)
        
    giphy_api = os.getenv('GIPHY')
    url = f"http://api.giphy.com/v1/gifs/search?q={job}&api_key={giphy_api}&limit=1&lang=ko"
    data = requests.get(url).json()
    img_url = data.get('data')[0].get('images').get('original').get('url')
    
    result['img_url'] = img_url

    return render(request, 'pastlife/pastlife.html', result)


