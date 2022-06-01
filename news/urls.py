from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # configured the url
    # path('welcome',views.welcome, name="homepage"),
    path('',views.newsOfToday, name="newsOfToday"),
    path('archives/<pastDate>', views.Pastnews, name = 'pastNews'),
    path('search',views.searchResult, name="searchResults"),
    path('article/<int:article_id>/', views.article, name="article"),
    path('accounts/', include('registration.backends.simple.urls')),
    path('new/article', views.new_article, name='new-article'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)