from django.test import TestCase
from django.utils.timezone import now


from .models import Movie


class GetResponseTest(TestCase):
    """
        Check if endpoints give valid status code with GET method.
    """
    def test_get_movies_response(self):
        self.assertEqual(self.client.get('/movies').status_code, 200)

    def test_get_top_response(self):
        self.assertEqual(self.client.get('/top').status_code, 200)

    def test_get_comments_response(self):
        self.assertEqual(self.client.get('/comments').status_code, 200)


class MoviesTest(TestCase):
    def test_add_new_movie_no_title(self):
        """
            Check if:
            - status code is 400
        """
        response = self.client.post('/movies', {})
        self.assertEqual(response.status_code, 400)

    def test_add_new_movie(self):
        """
            Check if:
            - status code is 201
            - returns title (changed to full/correct) and additional data from external database
            - object is added to database
        """
        response = self.client.post('/movies', {'title': 'Lord of the Rings'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['title'], 'The Lord of the Rings: The Fellowship of the Ring')
        self.assertEqual(response.data['rated'], 'PG-13')
        self.assertEqual(response.data['genre'], 'Adventure, Drama, Fantasy')
        self.assertEqual(response.data['director'], 'Peter Jackson')
        self.assertEqual(response.data['writer'],
            'J.R.R. Tolkien (novel), Fran Walsh (screenplay), Philippa Boyens (screenplay), Peter Jackson (screenplay)')
        self.assertTrue(Movie.objects.filter(title__icontains='The Lord of the Rings: The'))


class CommentTest(TestCase):
    def setUp(self):
        Movie.objects.create(title='NoExistingMovieName123')

    def test_add_new_comment_no_data(self):
        """
            Check if:
            - status code is 400
        """
        response = self.client.post('/comments')
        self.assertEqual(response.status_code, 400)

    def test_add_new_comment(self):
        """
            Check if:
            - status code is 201
            - returns comment data
            - object is added to database
        """
        movie_pk = Movie.objects.get(title='NoExistingMovieName123').pk
        response = self.client.post('/comments', {
            'nickname': 'Vader',
            'text': 'It should be longer.',
            'movie': movie_pk
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['nickname'], 'Vader')
        self.assertEqual(response.data['text'], 'It should be longer.')
        self.assertEqual(response.data['movie'], movie_pk)
        self.assertIn(now().strftime('%Y-%m-%d'), response.data['pub_date'])
        self.assertIn(now().strftime('%H:%M'), response.data['pub_date'])