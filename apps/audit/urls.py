# Rotas do módulo audit. Os nomes (name=) são usados nos templates — não renomear sem ajustar o HTML.
from django.urls import path
from . import views

app_name = 'audit'
urlpatterns = [
    path('logs/', views.logs_list, name='logs_list'),
]
