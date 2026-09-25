# Rotas do módulo finance. Os nomes (name=) são usados nos templates — não renomear sem ajustar o HTML.
from django.urls import path
from . import views

app_name = 'finance'
urlpatterns = [
    path('plans/', views.plans_list, name='plans_list'),
    path('plans/novo/', views.plans_create, name='plans_create'),
    path('plans/<uuid:pk>/editar/', views.plans_edit, name='plans_edit'),
    path('plans/<uuid:pk>/excluir/', views.plans_delete, name='plans_delete'),
    path('payments/', views.payments_list, name='payments_list'),
    path('payments/novo/', views.payments_create, name='payments_create'),
    path('payments/<uuid:pk>/editar/', views.payments_edit, name='payments_edit'),
    path('payments/<uuid:pk>/excluir/', views.payments_delete, name='payments_delete'),
    path('guardian-portal/', views.guardian_portal, name='guardian_portal'),
    path('segunda-via/<uuid:pk>/', views.second_copy, name='second_copy'),
]
