"""Views do módulo enrollments — STUBS. Implementar usando selectors.py (leitura) e services.py (escrita).
Toda view autenticada usa request.active_school; nunca ler school_id do POST/GET."""
from apps.core.htmx import htmx_saved, htmx_deleted  # noqa


def enrollments_list(request):
    """TELA 20 — listagem. Render: enrollments/enrollment_dashboard.html (se request.htmx: enrollments/partials/enrollments_table.html).
    Contexto: page_obj (Paginator), can{create,edit,delete}, filter_options. Ler via selectors, sempre com request.active_school."""
    raise NotImplementedError

def enrollments_create(request):
    """TELA 20 — GET: render components/_crud_form.html (form, form_title, action_url). POST válido: htmx_saved(); inválido: 422 + o mesmo template.
    Campos do ModelForm: status (edição); criação é feita na Tela 19. NÃO incluir 'school' no form: preencher com request.active_school no service."""
    raise NotImplementedError

def enrollments_edit(request, pk):
    """TELA 20 — igual a create, buscando o objeto pela escola ativa (404 se for de outra escola)."""
    raise NotImplementedError

def enrollments_delete(request, pk):
    """TELA 20 — hx-delete: excluir/inativar via service e devolver 200 com corpo vazio (a linha some) + auditoria."""
    raise NotImplementedError

def new_enrollment(request):
    """TELA 19 — Render: enrollments/new_enrollment.html. Contexto: form (student, academic_year, class_group); POST cria matrícula — o número (CODIGO-ESCOLA-ANO-SEQUENCIA) é gerado pelo banco"""
    raise NotImplementedError

def class_options(request):
    """TELA 19 — GET ?academic_year=<id>: devolve <select name='class_group'> só com turmas da escola ativa nesse ano."""
    raise NotImplementedError
