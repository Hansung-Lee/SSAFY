from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Score
from .forms import ScoreForm
from .serializer import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
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

    # res = requests.get(url_rank, headers=headers_naver)
    # res_data = res.json()
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
    return render(request, 'movies/list.html', {'movie1': movies[:4], 'movie2': movies[4:8], 'movie3': movies[8:]})


@api_view(['GET'])
def movie_list2(request):
    # 모든 음악들을 가져온다.
    movies = Movie.objects.all()
    # MusicSerializer(무엇을 시리얼라이즈할지, 여러개인지 한개인지)
    serializer = MovieSerializer(movies, many=True)

    # return render(request, 'list.html', {'musics': musics})
    return Response(data=serializer.data)


def detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})


@login_required
def create_score(request, movie_id):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, id=movie_id)
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
        return render(request, 'movies/update.html', {'form' : form})
