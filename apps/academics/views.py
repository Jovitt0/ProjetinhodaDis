"""Views do módulo academics — STUBS. Implementar usando selectors.py (leitura) e services.py (escrita).
Toda view autenticada usa request.active_school; nunca ler school_id do POST/GET."""
from apps.core.htmx import htmx_saved, htmx_deleted  # noqa


def courses_list(request):
    """TELA 10 — listagem. Render: academics/course_list.html (se request.htmx: academics/partials/courses_table.html).
    Contexto: page_obj (Paginator), can{create,edit,delete}, filter_options. Ler via selectors, sempre com request.active_school."""
    raise NotImplementedError

def courses_create(request):
    """TELA 10 — GET: render components/_crud_form.html (form, form_title, action_url). POST válido: htmx_saved(); inválido: 422 + o mesmo template.
    Campos do ModelForm: code, name, description, status. NÃO incluir 'school' no form: preencher com request.active_school no service."""
    raise NotImplementedError

def courses_edit(request, pk):
    """TELA 10 — igual a create, buscando o objeto pela escola ativa (404 se for de outra escola)."""
    raise NotImplementedError

def courses_delete(request, pk):
    """TELA 10 — hx-delete: excluir/inativar via service e devolver 200 com corpo vazio (a linha some) + auditoria."""
    raise NotImplementedError

def subjects_list(request):
    """TELA 11 — listagem. Render: academics/subject_list.html (se request.htmx: academics/partials/subjects_table.html).
    Contexto: page_obj (Paginator), can{create,edit,delete}, filter_options. Ler via selectors, sempre com request.active_school."""
    raise NotImplementedError

def subjects_create(request):
    """TELA 11 — GET: render components/_crud_form.html (form, form_title, action_url). POST válido: htmx_saved(); inválido: 422 + o mesmo template.
    Campos do ModelForm: course, code, name, description, status. NÃO incluir 'school' no form: preencher com request.active_school no service."""
    raise NotImplementedError

def subjects_edit(request, pk):
    """TELA 11 — igual a create, buscando o objeto pela escola ativa (404 se for de outra escola)."""
    raise NotImplementedError

def subjects_delete(request, pk):
    """TELA 11 — hx-delete: excluir/inativar via service e devolver 200 com corpo vazio (a linha some) + auditoria."""
    raise NotImplementedError

def classes_list(request):
    """TELA 12 — listagem. Render: academics/class_list.html (se request.htmx: academics/partials/classes_table.html).
    Contexto: page_obj (Paginator), can{create,edit,delete}, filter_options. Ler via selectors, sempre com request.active_school."""
    raise NotImplementedError

def classes_create(request):
    """TELA 12 — GET: render components/_crud_form.html (form, form_title, action_url). POST válido: htmx_saved(); inválido: 422 + o mesmo template.
    Campos do ModelForm: course, academic_year, code, name, grade_level. NÃO incluir 'school' no form: preencher com request.active_school no service."""
    raise NotImplementedError

def classes_edit(request, pk):
    """TELA 12 — igual a create, buscando o objeto pela escola ativa (404 se for de outra escola)."""
    raise NotImplementedError

def classes_delete(request, pk):
    """TELA 12 — hx-delete: excluir/inativar via service e devolver 200 com corpo vazio (a linha some) + auditoria."""
    raise NotImplementedError

def teachers_list(request):
    """TELA 13 — listagem. Render: academics/teacher_list.html (se request.htmx: academics/partials/teachers_table.html).
    Contexto: page_obj (Paginator), can{create,edit,delete}, filter_options. Ler via selectors, sempre com request.active_school."""
    raise NotImplementedError

def teachers_create(request):
    """TELA 13 — GET: render components/_crud_form.html (form, form_title, action_url). POST válido: htmx_saved(); inválido: 422 + o mesmo template.
    Campos do ModelForm: full_name, registration_number, document_number, user (opcional). NÃO incluir 'school' no form: preencher com request.active_school no service."""
    raise NotImplementedError

def teachers_edit(request, pk):
    """TELA 13 — igual a create, buscando o objeto pela escola ativa (404 se for de outra escola)."""
    raise NotImplementedError

def teachers_delete(request, pk):
    """TELA 13 — hx-delete: excluir/inativar via service e devolver 200 com corpo vazio (a linha some) + auditoria."""
    raise NotImplementedError

def assignments_list(request):
    """TELA 14 — listagem. Render: academics/teacher_assignments.html (se request.htmx: academics/partials/assignments_table.html).
    Contexto: page_obj (Paginator), can{create,edit,delete}, filter_options. Ler via selectors, sempre com request.active_school."""
    raise NotImplementedError

def assignments_create(request):
    """TELA 14 — GET: render components/_crud_form.html (form, form_title, action_url). POST válido: htmx_saved(); inválido: 422 + o mesmo template.
    Campos do ModelForm: teacher, class_group, subject, starts_on, ends_on, is_primary. NÃO incluir 'school' no form: preencher com request.active_school no service."""
    raise NotImplementedError

def assignments_edit(request, pk):
    """TELA 14 — igual a create, buscando o objeto pela escola ativa (404 se for de outra escola)."""
    raise NotImplementedError

def assignments_delete(request, pk):
    """TELA 14 — hx-delete: excluir/inativar via service e devolver 200 com corpo vazio (a linha some) + auditoria."""
    raise NotImplementedError
