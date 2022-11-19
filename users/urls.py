from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),

    path('account/', views.get_account, name='account'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),

    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>/', views.user_profile, name="user-profile"),

    path('add-skill/', views.add_skill, name='add-skill'),
    path('edit-skill/<str:pk>', views.edit_skill, name='edit-skill'),
    path('delete-skill/<str:pk>', views.delete_skill, name='delete-skill'),

]