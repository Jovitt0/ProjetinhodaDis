"""Views do módulo finance — STUBS. Implementar usando selectors.py (leitura) e services.py (escrita).
Toda view autenticada usa request.active_school; nunca ler school_id do POST/GET."""
from apps.core.htmx import htmx_saved, htmx_deleted  # noqa


def plans_list(request):
    """TELA 21 — listagem. Render: finance/contribution_plans.html (se request.htmx: finance/partials/plans_table.html).
    Contexto: page_obj (Paginator), can{create,edit,delete}, filter_options. Ler via selectors, sempre com request.active_school."""
    raise NotImplementedError

def plans_create(request):
    """TELA 21 — GET: render components/_crud_form.html (form, form_title, action_url). POST válido: htmx_saved(); inválido: 422 + o mesmo template.
    Campos do ModelForm: name, description, amount (reais → amount_cents), frequency, active. NÃO incluir 'school' no form: preencher com request.active_school no service."""
    raise NotImplementedError

def plans_edit(request, pk):
    """TELA 21 — igual a create, buscando o objeto pela escola ativa (404 se for de outra escola)."""
    raise NotImplementedError

def plans_delete(request, pk):
    """TELA 21 — hx-delete: excluir/inativar via service e devolver 200 com corpo vazio (a linha some) + auditoria."""
    raise NotImplementedError

def payments_list(request):
    """TELA 22 — listagem. Render: finance/payment_management.html (se request.htmx: finance/partials/payments_table.html).
    Contexto: page_obj (Paginator), can{create,edit,delete}, filter_options. Ler via selectors, sempre com request.active_school."""
    raise NotImplementedError

def payments_create(request):
    """TELA 22 — GET: render components/_crud_form.html (form, form_title, action_url). POST válido: htmx_saved(); inválido: 422 + o mesmo template.
    Campos do ModelForm: enrollment, responsible, contribution_plan, description, due_date, amount, status, paid_at, external_reference. NÃO incluir 'school' no form: preencher com request.active_school no service."""
    raise NotImplementedError

def payments_edit(request, pk):
    """TELA 22 — igual a create, buscando o objeto pela escola ativa (404 se for de outra escola)."""
    raise NotImplementedError

def payments_delete(request, pk):
    """TELA 22 — hx-delete: excluir/inativar via service e devolver 200 com corpo vazio (a linha some) + auditoria."""
    raise NotImplementedError

def guardian_portal(request):
    """TELA 23 — Render: finance/guardian_portal.html. Contexto: payments (pendentes e pagos do responsável), can_second_copy"""
    raise NotImplementedError

def second_copy(request, pk):
    """TELA 23 — segunda via da cobrança (só do responsável logado)."""
    raise NotImplementedError
