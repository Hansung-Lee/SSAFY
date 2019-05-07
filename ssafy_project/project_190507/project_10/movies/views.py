from django.shortcuts import render, get_object_or_404
from .models import Genre, Movie
from .serializer import GenreSerializer, MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def list_genre(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def genre_detail(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    movies = Movie.objects.filter(genre=genre).all()
    serializer = MovieSerializer(movies, many=True)
    
    return Response(data=serializer.data)
    

@api_view(['GET'])
def list_movie(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)
    

@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie)
    
    return Response(data=serializer.data)