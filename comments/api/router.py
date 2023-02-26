from rest_framework.routers import DefaultRouter

from comments.api.views import CommentApiView

routers_comments = DefaultRouter()

routers_comments.register(
    prefix='comments',
    basename='comments',
    viewset=CommentApiView
)
