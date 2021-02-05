from django.urls import path
from search import views

urlpatterns = [
    #path('', views.search, name='search'),
    path('search/', views.search, name='search_result'),
    path('', views.home, name='home'),
]
