"""Views do módulo students — STUBS. Implementar usando selectors.py (leitura) e services.py (escrita).
Toda view autenticada usa request.active_school; nunca ler school_id do POST/GET."""
from apps.core.htmx import htmx_saved, htmx_deleted  # noqa


def students_list(request):
    """TELA 15 — listagem. Render: students/student_list.html (se request.htmx: students/partials/students_table.html).
    Contexto: page_obj (Paginator), can{create,edit,delete}, filter_options. Ler via selectors, sempre com request.active_school."""
    raise NotImplementedError

def students_create(request):
    """TELA 15 — GET: render components/_crud_form.html (form, form_title, action_url). POST válido: htmx_saved(); inválido: 422 + o mesmo template.
    Campos do ModelForm: registration_number, full_name, social_name, birth_date, document_number, status. NÃO incluir 'school' no form: preencher com request.active_school no service."""
    raise NotImplementedError

def students_edit(request, pk):
    """TELA 15 — igual a create, buscando o objeto pela escola ativa (404 se for de outra escola)."""
    raise NotImplementedError

def students_delete(request, pk):
    """TELA 15 — hx-delete: excluir/inativar via service e devolver 200 com corpo vazio (a linha some) + auditoria."""
    raise NotImplementedError

def responsibles_list(request):
    """TELA 16 — listagem. Render: students/responsible_list.html (se request.htmx: students/partials/responsibles_table.html).
    Contexto: page_obj (Paginator), can{create,edit,delete}, filter_options. Ler via selectors, sempre com request.active_school."""
    raise NotImplementedError

def responsibles_create(request):
    """TELA 16 — GET: render components/_crud_form.html (form, form_title, action_url). POST válido: htmx_saved(); inválido: 422 + o mesmo template.
    Campos do ModelForm: full_name, document_number, email, phone (+ formset student_responsibles: student, relationship_type, is_primary). NÃO incluir 'school' no form: preencher com request.active_school no service."""
    raise NotImplementedError

def responsibles_edit(request, pk):
    """TELA 16 — igual a create, buscando o objeto pela escola ativa (404 se for de outra escola)."""
    raise NotImplementedError

def responsibles_delete(request, pk):
    """TELA 16 — hx-delete: excluir/inativar via service e devolver 200 com corpo vazio (a linha some) + auditoria."""
    raise NotImplementedError

def pickups_list(request):
    """TELA 17 — listagem. Render: students/pickup_authorizations.html (se request.htmx: students/partials/pickups_table.html).
    Contexto: page_obj (Paginator), can{create,edit,delete}, filter_options. Ler via selectors, sempre com request.active_school."""
    raise NotImplementedError

def pickups_create(request):
    """TELA 17 — GET: render components/_crud_form.html (form, form_title, action_url). POST válido: htmx_saved(); inválido: 422 + o mesmo template.
    Campos do ModelForm: student, authorized_name, document_number, relationship_type, valid_from, valid_until, is_active, notes. NÃO incluir 'school' no form: preencher com request.active_school no service."""
    raise NotImplementedError

def pickups_edit(request, pk):
    """TELA 17 — igual a create, buscando o objeto pela escola ativa (404 se for de outra escola)."""
    raise NotImplementedError

def pickups_delete(request, pk):
    """TELA 17 — hx-delete: excluir/inativar via service e devolver 200 com corpo vazio (a linha some) + auditoria."""
    raise NotImplementedError

def student_record(request, pk):
    """TELA 18 — Render: students/student_record.html. Contexto: student, secoes = [(id, título, url_name)] para as parciais student_record_enrollments/_guardians/_pickups (carregadas via HTMX)"""
    raise NotImplementedError

def student_record_enrollments(request, pk):
    """TELA 18 — parcial: matrículas do aluno."""
    raise NotImplementedError

def student_record_guardians(request, pk):
    """TELA 18 — parcial: responsáveis."""
    raise NotImplementedError

def student_record_pickups(request, pk):
    """TELA 18 — parcial: autorizações de retirada."""
    raise NotImplementedError
