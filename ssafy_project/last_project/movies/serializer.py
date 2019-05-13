from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'movie_code', 'movie_name_ko', 'movie_name_en', 'showTm', 'openDt',
                  'watch_grade_nm', 'audience', 'actors', 'directors', 'description', 'poster_url', 'genre']
