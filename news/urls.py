from django.urls import path
from . import views

urlpatterns = [
    # configured the url
    path('welcome',views.welcome, name="homepage"),
    path('',views.newsOfToday, name="newsOfToday"),
    path('/archives/(\d{4}-\d{2}-\d{2})/', views.Pastnews, name = 'pastNews'),

]