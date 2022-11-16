from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>/', views.user_profile, name="user-profile")

]