from django.contrib import admin
from blog import models
from .models import Post ,Event,Mission,Rating
from .models import User
from .models import Post ,Event,Mission , Image
from .models import user


admin.site.register(Event)
admin.site.register(Post)
admin.site.register(Mission)
admin.site.register(Rating)
#admin.site.register(User)
admin.site.register(Image)


@admin.register(models.user) #i deleted vaildid
class PlatformUsers(admin.ModelAdmin):
    pass


   