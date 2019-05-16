from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Score
from .forms import ScoreForm
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

from bs4 import BeautifulSoup as bs
import datetime
import requests


# Create your views here.
def movie_db(request):
    API_KEY = 'e4782a1ecd7ea361da31b4c4f2f5a02b'
    today = ''.join(str(datetime.date.today() - datetime.timedelta(days=1)).split('-'))  # 오늘 날짜

    url_boxoffice = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={}&targetDt={}&weekGb=0'.format(API_KEY, today)

    res = requests.get(url_boxoffice)
    res_data = res.json().get('boxOfficeResult').get('dailyBoxOfficeList')
    boxoffice = []
    audience = []
    for i in range(len(res_data)):
        boxoffice.append(res_data[i]['movieCd'])
        audience.append(res_data[i]['audiAcc'])

    movies = []
    for movie_code in boxoffice:
        url_movie = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={}&movieCd={}".format(API_KEY, movie_code)
        res = requests.get(url_movie)
        res_data = res.json().get('movieInfoResult').get('movieInfo')

        movies.append({
            'movie_code': res_data.get('movieCd'),
            'movie_name_ko': res_data.get('movieNm'),
            'movie_name_en': res_data.get('movieNmEn'),
            'showTm': res_data.get('showTm'),
            'openDt': '.'.join([res_data.get('openDt')[:4],res_data.get('openDt')[4:6],res_data.get('openDt')[6:]]),
            'genre': ', '.join([x['genreNm'] for x in res_data.get('genres')]),
            'watch_grade_nm': res_data.get('audits')[0].get('watchGradeNm'),
        })

    headers_naver = {
        'X-Naver-Client-Id': 'bS2KxFME66tpq5UJPclw',
        'X-Naver-Client-Secret': 'ZUOJVkLobP'
    }

    for i in range(len(movies)):
        url_naver = "https://openapi.naver.com/v1/search/movie.json?query={}".format(movies[i].get('movie_name_ko'))

        res = requests.get(url_naver, headers=headers_naver)
        res_data = res.json().get('items')

        if res_data:
            res_data = res_data[0]
            movies[i]['audience'] = audience[i]
            # movies[i]['score'] = res_data.get('userRating')
            movies[i]['actors'] = res_data.get('actor')[:-1]
            movies[i]['directors'] = res_data.get('director')[:-1]
            url_content = res_data.get('link')

            response = requests.get(url_content).text
            document = bs(response, 'html.parser')
            temp_content = document.select('.story_area .con_tx')
            content = str(temp_content)[19:-5].replace('\r', '').split('<br/>\xa0')
            movies[i]['description'] = '\n'.join(content)

            temp_img = document.select('.wide_info_area .poster')
            movies[i]['poster_url'] = str(temp_img).split('src=')[2].split('?type=')[0].replace('"', '')

    for movie_data in movies:
        movie = Movie()
        movie.movie_code = movie_data['movie_code']
        movie.movie_name_ko = movie_data['movie_name_ko']
        movie.movie_name_en = movie_data['movie_name_en']
        movie.showTm = movie_data['showTm']
        movie.openDt = movie_data['openDt']
        movie.watch_grade_nm = movie_data['watch_grade_nm']
        movie.audience = movie_data['audience']
        movie.actors = movie_data['actors']
        movie.directors = movie_data['directors']
        movie.description = movie_data['description']
        movie.poster_url = movie_data['poster_url']
        movie.genre = movie_data['genre']
        movie.save()

    return redirect('movies:movie_list')


def movie_db2(request):
    movie = {}

    url_rank = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'

    response = requests.get(url_rank).text
    document = bs(response, 'html.parser')
    temp_rank = document.select('.list_ranking .title a')

    temp_li = str(temp_rank).split('href="')[1:]
    for i in range(len(temp_li)):
        temp_li[i] = temp_li[i].split('" title')[0]

    for i in range(1):
        url_movie = 'https://movie.naver.com' + temp_li[i]
        response = requests.get(url_movie).text
        document = bs(response, 'html.parser')

        temp_content = document.select('.story_area .con_tx')
        content = str(temp_content)[19:-5].replace('\r', '').split('<br/>\xa0')
        movie['description'] = '\n'.join(content)

        temp_img = document.select('.wide_info_area .poster')
        movie['poster_url'] = str(temp_img).split('src=')[2].split('?type=')[0].replace('"', '')

        temp_title = document.select('.wide_info_area .mv_info .h_movie a')
        movie['movie_name_ko'] = str(temp_title).split('</a>')[0].split('">')[1]

    return render(request, 'movies/index.html')


def movie_list(request):
    movies = Movie.objects.all()[:10]
    return render(request, 'movies/list.html', {'movies': movies})


def detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.GET.get("theaterCode"):
        theatercode = request.GET.get("theaterCode")
    else:
        theatercode = '0056'

    url_movie = 'http://www.cgv.co.kr/theaters/'+f'?theaterCode={theatercode}'
    response = requests.get(url_movie).text
    document = bs(response, 'html.parser')

    temp_address = document.select('.wrap-theater .sect-theater .box-contents .title')
    address = str(temp_address).split('<br/>')[1].split('<a')[0]

    headers_naver_map = {
        'X-NCP-APIGW-API-KEY-ID': 'x8w0y9djtb',
        'X-NCP-APIGW-API-KEY': 'yD4XS0AedH9ShyGuFxMuI5UxqaKNzfrHapjviGkg'
    }

    url_geocode = f'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={address}'

    res = requests.get(url_geocode, headers=headers_naver_map)
    res_data = res.json()

    if not res_data.get('addresses'):
        url_movie = 'http://www.cgv.co.kr/theaters/' + f'?theaterCode={theatercode}'
        response = requests.get(url_movie).text
        document = bs(response, 'html.parser')

        temp_address = document.select('.wrap-theater .sect-theater .box-contents .title')
        address = '서울' + str(temp_address).split('서울')[1].split('<br/>')[0]

        url_geocode = f'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={address}'

        res = requests.get(url_geocode, headers=headers_naver_map)
        res_data = res.json()

    theaters = {
        '0056': 'CGV강남', '0001': 'CGV강변', '0229': 'CGV건대입구', '0010': 'CGV구로', '0063': 'CGV대학로',
        '0252': 'CGV동대문', '0230': 'CGV등촌', '0009': 'CGV명동', '0105': 'CGV명동역 씨네라이브러리', '0011': 'CGV목동',
        '0057': 'CGV미아', '0030': 'CGV불광', '0046': 'CGV상봉', '0083': 'CGV성신여대입구', '0088': 'CGV송파',
        '0276': 'CGV수유', '0150': 'CGV신촌아트레온', '0040': 'CGV압구정', '0112': 'CGV여의도', '0059': 'CGV영등포',
        '0074': 'CGV왕십리', '0013': 'CGV용산아이파크몰', '0131': 'CGV중계', '0199': 'CGV천호', '0107': 'CGV청담씨네시티',
        '0223': 'CGV피카디리1958', '0164': 'CGV하계', '0191': 'CGV홍대', '0040': 'CINE de CHEF 압구정', '0013': 'CINE de CHEF 용산아이파크몰',
        '0012': 'CGV수원', '0253': 'CGV해운대',
    }

    headers_naver = {
        'X-Naver-Client-Id': 'bS2KxFME66tpq5UJPclw',
        'X-Naver-Client-Secret': 'ZUOJVkLobP'
    }

    url_search = f'https://openapi.naver.com/v1/search/local.json?query={address} 맛집'
    res = requests.get(url_search, headers=headers_naver)
    restaurants = res.json().get('items')

    for r in restaurants:
        address = r.get('address')
        url_geocode = f'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={address}'

        res = requests.get(url_geocode, headers=headers_naver_map)
        res_data1 = res.json()
        r['x_axis'] = res_data1.get('addresses')[0].get('x')
        r['y_axis'] = res_data1.get('addresses')[0].get('y')

    sum_score = 0
    avg_score = 0
    list_score = movie.score_set.all()
    if list_score:
        for m_score in list_score:
            sum_score += m_score.value
        avg_score = round(sum_score / len(list_score), 2)

    context = {
        'movie': movie,
        'x_axis': res_data.get('addresses')[0].get('x'),
        'y_axis': res_data.get('addresses')[0].get('y'),
        'theater_code': theaters,
        'theater': theaters.get(str(theatercode)),
        'restaurants': restaurants,
        'avg_score': avg_score,
    }

    return render(request, 'movies/detail.html', context)


@login_required
def create_score(request, movie_id):
    if request.method == 'POST':
        score = ScoreForm(request.POST)
        if score.is_valid():
            form = score.save(commit=False)
            form.movie_id = movie_id
            form.user = request.user
            form.save()
            return redirect('movies:detail', movie_id=movie_id)
        return redirect('movies:detail', movie_id=movie_id)
    return redirect('movies:detail')


@login_required
def create_score(request, movie_id):
    if request.method == 'POST':
        score = ScoreForm(request.POST)
        if score.is_valid():
            form = score.save(commit=False)
            form.movie_id = movie_id
            form.user = request.user
            form.save()
            return redirect('movies:detail', movie_id=movie_id)
        return redirect('movies:detail', movie_id=movie_id)
    return redirect('movies:detail')


@login_required
def delete_score(request, movie_id, score_id):
    if request.method == 'POST':
        score = get_object_or_404(Score, id=score_id)
        score.delete()
        return redirect('movies:detail', movie_id=movie_id)
    return redirect('movies:movie_list')


@login_required
def update_score(request, score_id, movie_id):
    score = get_object_or_404(Score, id=score_id)
    movie = get_object_or_404(Movie, id=movie_id)
    if score.user != request.user:
        return HttpResponseForbidden("You are not allowed to update this Article")

    if request.method == 'POST':
        form = ScoreForm(request.POST, instance=score)
        if form.is_valid():
            score_form = form.save(commit=False)
            score_form.movie_id = movie_id
            score_form.user = request.user
            score_form.save()
            return redirect('movies:detail', movie_id=movie_id)
    else:
        form = ScoreForm(instance=score)
        return render(request, 'movies/update.html', {'form': form, 'movie': movie})
