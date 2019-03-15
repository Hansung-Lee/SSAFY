from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Score


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
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/edit.html', {'movie': movie})


def update(request, movie_id):
    title = request.GET.get('title')
    audience = request.GET.get('audience')
    poster_url = request.GET.get('poster_url')
    description = request.GET.get('description')

    movie = get_object_or_404(Movie, id=movie_id)
    movie.title = title
    movie.audience = audience
    movie.poster_url = poster_url
    movie.description = description

    movie.save()
    return redirect('movies:detail', movie_id)
