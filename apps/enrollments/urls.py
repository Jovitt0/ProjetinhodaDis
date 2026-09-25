# Rotas do módulo enrollments. Os nomes (name=) são usados nos templates — não renomear sem ajustar o HTML.
from django.urls import path
from . import views

app_name = 'enrollments'
urlpatterns = [
    path('enrollments/', views.enrollments_list, name='enrollments_list'),
    path('enrollments/novo/', views.enrollments_create, name='enrollments_create'),
    path('enrollments/<uuid:pk>/editar/', views.enrollments_edit, name='enrollments_edit'),
    path('enrollments/<uuid:pk>/excluir/', views.enrollments_delete, name='enrollments_delete'),
    path('new-enrollment/', views.new_enrollment, name='new_enrollment'),
    path('turmas-do-ano/', views.class_options, name='class_options'),
]
