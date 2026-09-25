# Rotas do módulo access. Os nomes (name=) são usados nos templates — não renomear sem ajustar o HTML.
from django.urls import path
from . import views

app_name = 'access'
urlpatterns = [
    path('users/', views.users_list, name='users_list'),
    path('users/novo/', views.users_create, name='users_create'),
    path('users/<uuid:pk>/editar/', views.users_edit, name='users_edit'),
    path('users/<uuid:pk>/excluir/', views.users_delete, name='users_delete'),
    path('memberships/', views.memberships_list, name='memberships_list'),
    path('memberships/novo/', views.memberships_create, name='memberships_create'),
    path('memberships/<uuid:pk>/editar/', views.memberships_edit, name='memberships_edit'),
    path('memberships/<uuid:pk>/excluir/', views.memberships_delete, name='memberships_delete'),
    path('permission-matrix/', views.permission_matrix, name='permission_matrix'),
    path('escolher-escola/', views.select_school, name='select_school'),
    path('permissoes/alternar/', views.permission_toggle, name='permission_toggle'),
]
