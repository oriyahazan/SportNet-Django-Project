from django.contrib import admin
from blog import models
from .models import Post ,Event,Mission
from .models import User


admin.site.register(Event)
admin.site.register(Post)
admin.site.register(Mission)
#admin.site.register(User)


@admin.register(models.User) #i deleted vaildid
class PlatformUsers(admin.ModelAdmin):
    pass


   