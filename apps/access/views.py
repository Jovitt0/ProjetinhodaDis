"""Views do módulo access — STUBS. Implementar usando selectors.py (leitura) e services.py (escrita).
Toda view autenticada usa request.active_school; nunca ler school_id do POST/GET."""
from apps.core.htmx import htmx_saved, htmx_deleted  # noqa


def users_list(request):
    """TELA 4 — listagem. Render: access/user_management.html (se request.htmx: access/partials/users_table.html).
    Contexto: page_obj (Paginator), can{create,edit,delete}, filter_options. Ler via selectors, sempre com request.active_school."""
    raise NotImplementedError

def users_create(request):
    """TELA 4 — GET: render components/_crud_form.html (form, form_title, action_url). POST válido: htmx_saved(); inválido: 422 + o mesmo template.
    Campos do ModelForm: full_name, email, status (+ formset de vínculos com escolas). NÃO incluir 'school' no form: preencher com request.active_school no service."""
    raise NotImplementedError

def users_edit(request, pk):
    """TELA 4 — igual a create, buscando o objeto pela escola ativa (404 se for de outra escola)."""
    raise NotImplementedError

def users_delete(request, pk):
    """TELA 4 — hx-delete: excluir/inativar via service e devolver 200 com corpo vazio (a linha some) + auditoria."""
    raise NotImplementedError

def memberships_list(request):
    """TELA 5 — listagem. Render: access/roles_management.html (se request.htmx: access/partials/memberships_table.html).
    Contexto: page_obj (Paginator), can{create,edit,delete}, filter_options. Ler via selectors, sempre com request.active_school."""
    raise NotImplementedError

def memberships_create(request):
    """TELA 5 — GET: render components/_crud_form.html (form, form_title, action_url). POST válido: htmx_saved(); inválido: 422 + o mesmo template.
    Campos do ModelForm: roles (múltipla escolha), status. NÃO incluir 'school' no form: preencher com request.active_school no service."""
    raise NotImplementedError

def memberships_edit(request, pk):
    """TELA 5 — igual a create, buscando o objeto pela escola ativa (404 se for de outra escola)."""
    raise NotImplementedError

def memberships_delete(request, pk):
    """TELA 5 — hx-delete: excluir/inativar via service e devolver 200 com corpo vazio (a linha some) + auditoria."""
    raise NotImplementedError

def permission_matrix(request):
    """TELA 6 — Render: access/permission_matrix.html. Contexto: roles (lista), matrix {recurso: [{permission, cells: [{role, granted}]}]}; só Admin Global"""
    raise NotImplementedError

def select_school(request):
    """TELA 2 — GET lista vínculos ativos; POST membership_id → valida vínculo/escola ativa → grava na sessão."""
    raise NotImplementedError

def permission_toggle(request):
    """TELA 6 — hx-post role+permission: cria/remove role_permissions. Só Admin Global. Responde 204."""
    raise NotImplementedError
