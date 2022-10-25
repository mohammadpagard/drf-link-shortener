from django.urls import path
from . import views


app_name = 'shortener'
urlpatterns = [
    path('', views.LinkShortenerView.as_view(), name='long_url'),
    path('<short_url>/', views.ShortenerView.as_view(), name='short_url'),
]
