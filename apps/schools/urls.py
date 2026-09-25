# Rotas do módulo schools. Os nomes (name=) são usados nos templates — não renomear sem ajustar o HTML.
from django.urls import path
from . import views

app_name = 'schools'
urlpatterns = [
    path('schools/', views.schools_list, name='schools_list'),
    path('schools/novo/', views.schools_create, name='schools_create'),
    path('schools/<uuid:pk>/editar/', views.schools_edit, name='schools_edit'),
    path('schools/<uuid:pk>/excluir/', views.schools_delete, name='schools_delete'),
    path('academic_years/', views.academic_years_list, name='academic_years_list'),
    path('academic_years/novo/', views.academic_years_create, name='academic_years_create'),
    path('academic_years/<uuid:pk>/editar/', views.academic_years_edit, name='academic_years_edit'),
    path('academic_years/<uuid:pk>/excluir/', views.academic_years_delete, name='academic_years_delete'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
