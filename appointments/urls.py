from django.urls import path
from appointments import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('cadastro/', views.create_citizen, name='cadastro'),
    path('logout/', views.logout_user, name='logout'),
    path('pesquisar_agendamento/', views.check_appointment, name='pesquisar_agendamento'),
    path('realizar_agendamento/', views.create_appointment, name='realizar_agendamento'),
    path('ver_agendamento/', views.show_appointment, name='ver_agendamento'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]
