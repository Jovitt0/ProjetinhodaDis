"""Perfis de acesso simulados para o preview (troca no seletor do topo).
Fonte da matriz: LEVANTAMENTO_REQUISITOS_FUNCIONAIS.md, seção 17 — Matriz resumida de permissões.
No backend real isto vira a leitura de user_school_roles + role_permissions para a escola ativa."""

CATEGORY_OF = {  # recurso (nome usado nas urls) -> categoria da matriz de permissões
    "users": "usuarios", "memberships": "usuarios",
    "schools": "escolas", "academic_years": "escolas",
    "courses": "turmas", "subjects": "turmas", "classes": "turmas", "assignments": "professores",
    "teachers": "professores",
    "students": "alunos", "responsibles": "alunos", "pickups": "alunos",
    "enrollments": "matriculas",
    "plans": "financeiro", "payments": "financeiro",
    "activities": "privacidade", "retention": "privacidade", "dsar": "privacidade", "incidents": "privacidade",
    "logs": "auditoria",
}
APP_OF_CATEGORY = {  # categoria -> app dono do grupo na barra lateral
    "usuarios": "access", "escolas": "schools", "turmas": "academics", "professores": "academics",
    "alunos": "students", "matriculas": "enrollments", "financeiro": "finance",
    "privacidade": "privacy", "auditoria": "audit",
}
V = lambda view, edit: {"view": view, "edit": edit}
MATRIX = {
    "master":     {c: V(True, True) for c in APP_OF_CATEGORY},
    "diretor":    {"usuarios": V(False, False), "escolas": V(True, False), "alunos": V(True, True),
                   "matriculas": V(True, True), "turmas": V(True, True), "professores": V(True, True),
                   "financeiro": V(True, True), "privacidade": V(True, True), "auditoria": V(True, False)},
    "secretaria": {"usuarios": V(False, False), "escolas": V(True, False), "alunos": V(True, True),
                   "matriculas": V(True, True), "turmas": V(True, True), "professores": V(True, False),
                   "financeiro": V(True, False), "privacidade": V(False, False), "auditoria": V(False, False)},
    "financeiro": {"usuarios": V(False, False), "escolas": V(True, False), "alunos": V(True, False),
                   "matriculas": V(False, False), "turmas": V(False, False), "professores": V(False, False),
                   "financeiro": V(True, True), "privacidade": V(False, False), "auditoria": V(False, False)},
    "professor":  {"usuarios": V(False, False), "escolas": V(True, False), "alunos": V(True, False),
                   "matriculas": V(True, False), "turmas": V(True, False), "professores": V(True, False),
                   "financeiro": V(False, False), "privacidade": V(False, False), "auditoria": V(False, False)},
    "consulta":   {"usuarios": V(False, False), "escolas": V(True, False), "alunos": V(True, False),
                   "matriculas": V(True, False), "turmas": V(True, False), "professores": V(True, False),
                   "financeiro": V(True, False), "privacidade": V(False, False), "auditoria": V(False, False)},
}
LABELS = {"master": "Administrador geral", "diretor": "Administrador da escola", "secretaria": "Secretaria",
          "financeiro": "Financeiro", "professor": "Professor", "consulta": "Somente consulta"}


def current_role(request):
    return request.session.get("preview_role", "master")


def can_for(role, resource):
    """can{create,edit,delete} para a tela do 'resource' informado (ex.: 'students')."""
    cat = CATEGORY_OF.get(resource)
    perm = MATRIX.get(role, MATRIX["consulta"]).get(cat, V(False, False))
    return {"create": perm["edit"], "edit": perm["edit"], "delete": perm["edit"]}


def nav_for(role):
    """{app: bool} usado pela barra lateral para mostrar/esconder cada grupo de módulo."""
    m = MATRIX.get(role, MATRIX["consulta"])
    nav = {app: False for app in set(APP_OF_CATEGORY.values())}
    for cat, perm in m.items():
        if perm["view"]:
            nav[APP_OF_CATEGORY[cat]] = True
    nav["schools"] = True  # Visão geral sempre acessível, mesmo quando "Escolas" ficaria escondido
    return nav


def edit_for(role):
    """{categoria: bool} usado para esconder atalhos de criação (ex.: 'Nova matrícula') na barra lateral."""
    return {cat: perm["edit"] for cat, perm in MATRIX.get(role, MATRIX["consulta"]).items()}