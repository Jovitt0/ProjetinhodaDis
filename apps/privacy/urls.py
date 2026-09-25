# Rotas do módulo privacy. Os nomes (name=) são usados nos templates — não renomear sem ajustar o HTML.
from django.urls import path
from . import views

app_name = 'privacy'
urlpatterns = [
    path('activities/', views.activities_list, name='activities_list'),
    path('activities/novo/', views.activities_create, name='activities_create'),
    path('activities/<uuid:pk>/editar/', views.activities_edit, name='activities_edit'),
    path('activities/<uuid:pk>/excluir/', views.activities_delete, name='activities_delete'),
    path('retention/', views.retention_list, name='retention_list'),
    path('retention/novo/', views.retention_create, name='retention_create'),
    path('retention/<uuid:pk>/editar/', views.retention_edit, name='retention_edit'),
    path('retention/<uuid:pk>/excluir/', views.retention_delete, name='retention_delete'),
    path('dsar/', views.dsar_list, name='dsar_list'),
    path('dsar/novo/', views.dsar_create, name='dsar_create'),
    path('dsar/<uuid:pk>/editar/', views.dsar_edit, name='dsar_edit'),
    path('dsar/<uuid:pk>/excluir/', views.dsar_delete, name='dsar_delete'),
    path('incidents/', views.incidents_list, name='incidents_list'),
    path('incidents/novo/', views.incidents_create, name='incidents_create'),
    path('incidents/<uuid:pk>/editar/', views.incidents_edit, name='incidents_edit'),
    path('incidents/<uuid:pk>/excluir/', views.incidents_delete, name='incidents_delete'),
]
