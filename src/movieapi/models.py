from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    rated = models.CharField(max_length=10, default='')
    genre = models.CharField(max_length=50, default='')
    director = models.CharField(max_length=50, default='')
    writer = models.CharField(max_length=50, default='')

    def __str__(self):
        return f'(id: {self.pk}) {self.title}'


class Comment(models.Model):
    movie = models.ForeignKey(Movie, related_name='comments', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
