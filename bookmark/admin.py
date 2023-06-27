from django.contrib import admin

from bookmark.models import Bookmark

# Register your models here.
# 데코레이터 패턴 사용하지 않는 방법
# admin.site.register(Bookmark,BookmarkAdmin)

# 데코레이터 패턴 사용하는 방법
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id','title','url')
