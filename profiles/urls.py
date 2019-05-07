from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'profile'),
    path('<int:user_id>/', views.user_profile, name= 'user_profile'),
    path('register/', views.register, name= 'register'),
    path('login/', views.login, name= 'login'),
    path('logout/', views.logOut, name= 'logOut'),
]