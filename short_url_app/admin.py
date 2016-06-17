from django.contrib import admin

# Register your models here.
from short_url_app.models import Click, Bookmark

admin.site.register(Click)
admin.site.register(Bookmark)
