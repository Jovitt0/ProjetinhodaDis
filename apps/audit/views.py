"""Views do módulo audit — STUBS. Implementar usando selectors.py (leitura) e services.py (escrita).
Toda view autenticada usa request.active_school; nunca ler school_id do POST/GET."""
from apps.core.htmx import htmx_saved, htmx_deleted  # noqa


def logs_list(request):
    """TELA 28 — listagem. Render: audit/audit_logs.html (se request.htmx: audit/partials/logs_table.html).
    Contexto: page_obj (Paginator), can{create,edit,delete}, filter_options. Ler via selectors, sempre com request.active_school."""
    raise NotImplementedError
