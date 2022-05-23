from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # configured the url
    # path('welcome',views.welcome, name="homepage"),
    path('',views.newsOfToday, name="newsOfToday"),
    path('/archives/(\d{4}-\d{2}-\d{2})/', views.Pastnews, name = 'pastNews'),
    path('search',views.searchResult, name="searchResults"),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)