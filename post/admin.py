from django.contrib import admin
from .models import (
    Blog,
    PostView,
    Like,
    Comment,
    User
)


admin.site.register(Blog)
admin.site.register(User)
admin.site.register(PostView)
admin.site.register(Like)
admin.site.register(Comment)
