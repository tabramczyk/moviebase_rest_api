from rest_framework import serializers
from .models import Movie, Comment


class MovieSerializer(serializers.ModelSerializer):
    movie_id = serializers.IntegerField(read_only=True, source='pk')
    class Meta:
        model = Movie
        fields = ('movie_id', 'title', 'rated', 'genre', 'director', 'writer')
        read_only_fields = ('rated', 'genre', 'director', 'writer')


class CommentSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(many=False,
                                               queryset=Movie.objects.all(),
                                               read_only=False)
    class Meta:
        model = Comment
        fields = ('nickname', 'text', 'pub_date', 'movie')
        read_only_fields = ('pub_date',)


class TopSerializer(serializers.ModelSerializer):
    rank = serializers.IntegerField(read_only=True)
    total_comments = serializers.IntegerField(read_only=True)
    movie_id = serializers.IntegerField(read_only=True, source='pk')
    class Meta:
        model = Movie
        fields = ('movie_id', 'total_comments', 'rank')