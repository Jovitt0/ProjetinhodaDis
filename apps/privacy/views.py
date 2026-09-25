"""Views do módulo privacy — STUBS. Implementar usando selectors.py (leitura) e services.py (escrita).
Toda view autenticada usa request.active_school; nunca ler school_id do POST/GET."""
from apps.core.htmx import htmx_saved, htmx_deleted  # noqa


def activities_list(request):
    """TELA 24 — listagem. Render: privacy/processing_activities.html (se request.htmx: privacy/partials/activities_table.html).
    Contexto: page_obj (Paginator), can{create,edit,delete}, filter_options. Ler via selectors, sempre com request.active_school."""
    raise NotImplementedError

def activities_create(request):
    """TELA 24 — GET: render components/_crud_form.html (form, form_title, action_url). POST válido: htmx_saved(); inválido: 422 + o mesmo template.
    Campos do ModelForm: name, purpose, legal_basis, data_categories (JSON), retention_rule, active. NÃO incluir 'school' no form: preencher com request.active_school no service."""
    raise NotImplementedError

def activities_edit(request, pk):
    """TELA 24 — igual a create, buscando o objeto pela escola ativa (404 se for de outra escola)."""
    raise NotImplementedError

def activities_delete(request, pk):
    """TELA 24 — hx-delete: excluir/inativar via service e devolver 200 com corpo vazio (a linha some) + auditoria."""
    raise NotImplementedError

def retention_list(request):
    """TELA 25 — listagem. Render: privacy/retention_rules.html (se request.htmx: privacy/partials/retention_table.html).
    Contexto: page_obj (Paginator), can{create,edit,delete}, filter_options. Ler via selectors, sempre com request.active_school."""
    raise NotImplementedError

def retention_create(request):
    """TELA 25 — GET: render components/_crud_form.html (form, form_title, action_url). POST válido: htmx_saved(); inválido: 422 + o mesmo template.
    Campos do ModelForm: name, entity_type, retention_days, disposal_action, active. NÃO incluir 'school' no form: preencher com request.active_school no service."""
    raise NotImplementedError

def retention_edit(request, pk):
    """TELA 25 — igual a create, buscando o objeto pela escola ativa (404 se for de outra escola)."""
    raise NotImplementedError

def retention_delete(request, pk):
    """TELA 25 — hx-delete: excluir/inativar via service e devolver 200 com corpo vazio (a linha some) + auditoria."""
    raise NotImplementedError

def dsar_list(request):
    """TELA 26 — listagem. Render: privacy/dsar_requests.html (se request.htmx: privacy/partials/dsar_table.html).
    Contexto: page_obj (Paginator), can{create,edit,delete}, filter_options. Ler via selectors, sempre com request.active_school."""
    raise NotImplementedError

def dsar_create(request):
    """TELA 26 — GET: render components/_crud_form.html (form, form_title, action_url). POST válido: htmx_saved(); inválido: 422 + o mesmo template.
    Campos do ModelForm: requester_name, requester_document, request_type, description, status, completed_at. NÃO incluir 'school' no form: preencher com request.active_school no service."""
    raise NotImplementedError

def dsar_edit(request, pk):
    """TELA 26 — igual a create, buscando o objeto pela escola ativa (404 se for de outra escola)."""
    raise NotImplementedError

def dsar_delete(request, pk):
    """TELA 26 — hx-delete: excluir/inativar via service e devolver 200 com corpo vazio (a linha some) + auditoria."""
    raise NotImplementedError

def incidents_list(request):
    """TELA 27 — listagem. Render: privacy/security_incidents.html (se request.htmx: privacy/partials/incidents_table.html).
    Contexto: page_obj (Paginator), can{create,edit,delete}, filter_options. Ler via selectors, sempre com request.active_school."""
    raise NotImplementedError

def incidents_create(request):
    """TELA 27 — GET: render components/_crud_form.html (form, form_title, action_url). POST válido: htmx_saved(); inválido: 422 + o mesmo template.
    Campos do ModelForm: title, description, severity, occurred_at, resolved_at, status. NÃO incluir 'school' no form: preencher com request.active_school no service."""
    raise NotImplementedError

def incidents_edit(request, pk):
    """TELA 27 — igual a create, buscando o objeto pela escola ativa (404 se for de outra escola)."""
    raise NotImplementedError

def incidents_delete(request, pk):
    """TELA 27 — hx-delete: excluir/inativar via service e devolver 200 com corpo vazio (a linha some) + auditoria."""
    raise NotImplementedError
