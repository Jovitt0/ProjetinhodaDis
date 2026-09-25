# Rotas do módulo students. Os nomes (name=) são usados nos templates — não renomear sem ajustar o HTML.
from django.urls import path
from . import views

app_name = 'students'
urlpatterns = [
    path('students/', views.students_list, name='students_list'),
    path('students/novo/', views.students_create, name='students_create'),
    path('students/<uuid:pk>/editar/', views.students_edit, name='students_edit'),
    path('students/<uuid:pk>/excluir/', views.students_delete, name='students_delete'),
    path('responsibles/', views.responsibles_list, name='responsibles_list'),
    path('responsibles/novo/', views.responsibles_create, name='responsibles_create'),
    path('responsibles/<uuid:pk>/editar/', views.responsibles_edit, name='responsibles_edit'),
    path('responsibles/<uuid:pk>/excluir/', views.responsibles_delete, name='responsibles_delete'),
    path('pickups/', views.pickups_list, name='pickups_list'),
    path('pickups/novo/', views.pickups_create, name='pickups_create'),
    path('pickups/<uuid:pk>/editar/', views.pickups_edit, name='pickups_edit'),
    path('pickups/<uuid:pk>/excluir/', views.pickups_delete, name='pickups_delete'),
    path('alunos/<uuid:pk>/ficha/', views.student_record, name='student_record'),
    path('alunos/<uuid:pk>/ficha/matriculas/', views.student_record_enrollments, name='student_record_enrollments'),
    path('alunos/<uuid:pk>/ficha/responsaveis/', views.student_record_guardians, name='student_record_guardians'),
    path('alunos/<uuid:pk>/ficha/retiradas/', views.student_record_pickups, name='student_record_pickups'),
]
