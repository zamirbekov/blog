from django.contrib import admin
from django.conf import settings
from django.urls import include, path, re_path

from articles import views as articles_views
from comments import views as comment_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', articles_views.index, name='index'),
    path('<slug:title>/', articles_views.category, name='category'),
    path('article/<int:id>/', articles_views.single_article, name='single_article'),
    path('article/addcomment/<int:article_id>/', comment_views.add_comment, name='add_comment'),
    path('search_results/', articles_views.search_results, name='search_results'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns