from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.signin, name='login'),
    path('register', views.register, name='register'),
    path('add_qst', views.add_qst, name='add_qst'),
    path('logout', views.logoutUser, name='logout'),
    path('send_email', views.send_email, name='send_email'),

]