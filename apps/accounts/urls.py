# TELAS 1 e 3. Views de login/logout/profile/password_change: a equipe de backend implementa (usar templates/accounts/*.html).
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('entrar/', views.login_view, name='login'),
    path('sair/', views.logout_view, name='logout'),   # POST
    path('perfil/', views.profile, name='profile'),
    path('perfil/senha/', views.password_change, name='password_change'),
]
