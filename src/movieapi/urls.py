from rest_framework import routers
from .views import MovieViewSet, CommentViewSet, TopViewSet, redirect_view


router = routers.DefaultRouter(trailing_slash = False)

router.register('movies', MovieViewSet)
router.register('top', TopViewSet)
router.register('comments', CommentViewSet)



urlpatterns = router.urls
