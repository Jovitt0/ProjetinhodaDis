"""Views do módulo schools — STUBS. Implementar usando selectors.py (leitura) e services.py (escrita).
Toda view autenticada usa request.active_school; nunca ler school_id do POST/GET."""
from apps.core.htmx import htmx_saved, htmx_deleted  # noqa


def schools_list(request):
    """TELA 7 — listagem. Render: schools/school_list.html (se request.htmx: schools/partials/schools_table.html).
    Contexto: page_obj (Paginator), can{create,edit,delete}, filter_options. Ler via selectors, sempre com request.active_school."""
    raise NotImplementedError

def schools_create(request):
    """TELA 7 — GET: render components/_crud_form.html (form, form_title, action_url). POST válido: htmx_saved(); inválido: 422 + o mesmo template.
    Campos do ModelForm: code, name, legal_name, document_number, status, timezone. NÃO incluir 'school' no form: preencher com request.active_school no service."""
    raise NotImplementedError

def schools_edit(request, pk):
    """TELA 7 — igual a create, buscando o objeto pela escola ativa (404 se for de outra escola)."""
    raise NotImplementedError

def schools_delete(request, pk):
    """TELA 7 — hx-delete: excluir/inativar via service e devolver 200 com corpo vazio (a linha some) + auditoria."""
    raise NotImplementedError

def academic_years_list(request):
    """TELA 8 — listagem. Render: schools/academic_years.html (se request.htmx: schools/partials/academic_years_table.html).
    Contexto: page_obj (Paginator), can{create,edit,delete}, filter_options. Ler via selectors, sempre com request.active_school."""
    raise NotImplementedError

def academic_years_create(request):
    """TELA 8 — GET: render components/_crud_form.html (form, form_title, action_url). POST válido: htmx_saved(); inválido: 422 + o mesmo template.
    Campos do ModelForm: year, name, starts_on, ends_on, status. NÃO incluir 'school' no form: preencher com request.active_school no service."""
    raise NotImplementedError

def academic_years_edit(request, pk):
    """TELA 8 — igual a create, buscando o objeto pela escola ativa (404 se for de outra escola)."""
    raise NotImplementedError

def academic_years_delete(request, pk):
    """TELA 8 — hx-delete: excluir/inativar via service e devolver 200 com corpo vazio (a linha some) + auditoria."""
    raise NotImplementedError

def dashboard(request):
    """TELA 9 — Render: schools/dashboard.html. Contexto: metrics {enrolled, active_classes, overdue_payments, overdue_amount_display}"""
    raise NotImplementedError
