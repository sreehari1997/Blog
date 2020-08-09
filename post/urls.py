from django.urls import path, include
from post.views import (
    BlogUpdateView,
    BlogCreateView,
    BlogDeleteView,
    BlogListView,
    BlogDetailView,
    like_post
)

urlpatterns = [
    path('', BlogListView.as_view(), name="list"),
    path('create/', BlogCreateView.as_view(), name="create"),
    path('<slug>/', BlogDetailView.as_view(), name="detail"),
    path('<slug>/update/', BlogUpdateView.as_view(), name="update"),
    path('<slug>/delete/', BlogDeleteView.as_view(), name="delete"),
    path('<slug>/like', like_post, name="like_post")
]