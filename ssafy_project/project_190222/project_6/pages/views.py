from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, 'pages/index.html', {'movies': movies})
    
def detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request, 'pages/detail.html', {'movie': movie})
    
def delete(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    movie.delete()
    return redirect('pages:index')
    
def new(request):
    return render(request, 'pages/new.html')
    
def create(request):
    title = request.GET.get('title')
    audience = request.GET.get('audience')
    genre = request.GET.get('genre')
    score = request.GET.get('score')
    poster_url = request.GET.get('poster_url')
    description = request.GET.get('description')
    
    Movie.objects.create(title=title, audience=audience, genre=genre, score=score, poster_url=poster_url, description=description)
    return render(request, 'pages/success.html')
    
def edit(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request, 'pages/edit.html', {'movie': movie})
    
def update(request, movie_id):
    title = request.GET.get('title')
    audience = request.GET.get('audience')
    genre = request.GET.get('genre')
    score = request.GET.get('score')
    poster_url = request.GET.get('poster_url')
    description = request.GET.get('description')
    
    movie = Movie.objects.get(pk=movie_id)
    movie.title = title
    movie.audience = audience
    movie.genre = genre
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description
    
    movie.save()
    return redirect('pages:detail', movie_id)