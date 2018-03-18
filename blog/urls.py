from django.contrib import admin
from django.conf import settings
from django.urls import include, path, re_path
from articles import views as articles_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', articles_views.index, name='index'),
    path('article/<int:id>/', articles_views.single_article, name='single_article'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns