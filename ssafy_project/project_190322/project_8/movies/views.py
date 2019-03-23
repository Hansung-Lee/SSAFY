from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Movie, Score
from .forms import MovieForm


# Create your views here.
def first(request):
    return redirect('movies:index')


def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    scores = movie.score_set.all()

    return render(request, 'movies/detail.html', {'movie': movie, 'scores': scores})


def delete(request, movie_id):
    if request.method == "POST":
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie_id)


def create_score(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == "POST":
        s = Score()
        s.content = request.POST.get('content')
        s.score = request.POST.get('score')
        s.movie_id = movie
        s.save()

    return redirect('movies:detail', movie_id)


def delete_score(request, movie_id, score_id):
    if request.method == "POST":
        s = get_object_or_404(Score, id=score_id)
        s.delete()

    return redirect('movies:detail', movie_id)


def edit(request, movie_id):
    if request.method == "POST":
        movie = get_object_or_404(Movie, id=movie_id)
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie_id)
        else:
            messages.warning(request, '영화 정보 수정 실패, 다시 시도해 주세요.')
            return redirect('movies:edit', movie_id)

    else:
        movie = get_object_or_404(Movie, id=movie_id)
        form = MovieForm(instance=movie)

        return render(request, 'movies/form.html', {'form': form})


def new(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', form.instance.id)
        else:
            messages.warning(request, '영화 정보 작성 실패, 다시 시도해 주세요.')
            return redirect('movies:new')

    else:
        form = MovieForm()

        return render(request, 'movies/form.html', {'form': form})
