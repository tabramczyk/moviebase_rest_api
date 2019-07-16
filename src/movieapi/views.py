from rest_framework import viewsets, status, filters
from rest_framework.response import Response
import requests
from urllib.parse import quote
from django.db.models import Count, F
from django.db.models.functions import RowNumber
from django.db.models.expressions import Window
from django.shortcuts import redirect


from .models import Movie, Comment
from .serializers import MovieSerializer, CommentSerializer, TopSerializer



def redirect_view(request):
    response = redirect('/movie')
    return response


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    http_method_names = ['get', 'post']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['title', 'director', 'writer']
    ordering_fields = ('title', 'rated')

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            title = quote(request.data['title'])
            r = requests.get(f'http://www.omdbapi.com/?apikey=f6918842&t={title}')
            omdbapi_data = r.json()
            if r.status_code == 200 and omdbapi_data['Response']=='True':
                serializer.save(
                    title=omdbapi_data['Title'],
                    rated=omdbapi_data['Rated'],
                    genre=omdbapi_data['Genre'],
                    director=omdbapi_data['Director'],
                    writer=omdbapi_data['Writer']
                )
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(r.json(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ['=movie__id',]
    http_method_names = ['get', 'post']


class TopViewSet(viewsets.ModelViewSet):
    serializer_class = TopSerializer
    queryset = Movie.objects.annotate(total_comments=Count('comments'),
                                      rank=Window(
                                          expression=RowNumber(),
                                          order_by=F('total_comments').desc()
                                      )).order_by('-total_comments')[:10]
    http_method_names = ['get']