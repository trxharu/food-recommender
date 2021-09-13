from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.welcome),
    path('api/recommender', views.getRecommendations)
]
