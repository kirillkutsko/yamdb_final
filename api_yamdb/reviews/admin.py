from django.contrib import admin

from .models import User
from .models import Review, Comment

admin.site.register(User)
admin.site.register(Review)
admin.site.register(Comment)
