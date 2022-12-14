from django.contrib import admin
from blog import models
from .models import Post
from .models import User



admin.site.register(Post)
#admin.site.register(Post)
#admin.site.register(User)


@admin.register(models.User) #i deleted vaildid
class PlatformUsers(admin.ModelAdmin):
    pass
   