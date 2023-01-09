from django.contrib import admin
from blog import models
from .models import Post ,Event,Mission , Image, Rating,CreateGuide, Donate
from .models import user


admin.site.register(Event)
admin.site.register(CreateGuide)
admin.site.register(Post)
admin.site.register(Mission)
admin.site.register(Rating)
admin.site.register(Image)
admin.site.register(Donate)


@admin.register(models.user) #i deleted vaildid
class PlatformUsers(admin.ModelAdmin):
    pass


   