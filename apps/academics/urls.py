# Rotas do módulo academics. Os nomes (name=) são usados nos templates — não renomear sem ajustar o HTML.
from django.urls import path
from . import views

app_name = 'academics'
urlpatterns = [
    path('courses/', views.courses_list, name='courses_list'),
    path('courses/novo/', views.courses_create, name='courses_create'),
    path('courses/<uuid:pk>/editar/', views.courses_edit, name='courses_edit'),
    path('courses/<uuid:pk>/excluir/', views.courses_delete, name='courses_delete'),
    path('subjects/', views.subjects_list, name='subjects_list'),
    path('subjects/novo/', views.subjects_create, name='subjects_create'),
    path('subjects/<uuid:pk>/editar/', views.subjects_edit, name='subjects_edit'),
    path('subjects/<uuid:pk>/excluir/', views.subjects_delete, name='subjects_delete'),
    path('classes/', views.classes_list, name='classes_list'),
    path('classes/novo/', views.classes_create, name='classes_create'),
    path('classes/<uuid:pk>/editar/', views.classes_edit, name='classes_edit'),
    path('classes/<uuid:pk>/excluir/', views.classes_delete, name='classes_delete'),
    path('teachers/', views.teachers_list, name='teachers_list'),
    path('teachers/novo/', views.teachers_create, name='teachers_create'),
    path('teachers/<uuid:pk>/editar/', views.teachers_edit, name='teachers_edit'),
    path('teachers/<uuid:pk>/excluir/', views.teachers_delete, name='teachers_delete'),
    path('assignments/', views.assignments_list, name='assignments_list'),
    path('assignments/novo/', views.assignments_create, name='assignments_create'),
    path('assignments/<uuid:pk>/editar/', views.assignments_edit, name='assignments_edit'),
    path('assignments/<uuid:pk>/excluir/', views.assignments_delete, name='assignments_delete'),
]
