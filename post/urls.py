from django.urls import path, include
from post.views import post_view, index_view

urlpatterns = [
    path('', index_view),
    path('blog/', post_view),
]