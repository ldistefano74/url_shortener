from django.urls import path
from . import views


urlpatterns = [
    path('store/', views.store),
    path('redirect/', views.redirect_id),
    path('statistics', views.stats),
]