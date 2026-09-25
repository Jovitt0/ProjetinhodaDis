"""Context processor de PRÉ-VISUALIZAÇÃO: calcula nav/edit a partir do perfil simulado (seletor no topo).
No backend real isto vira o cálculo de permissões da escola ativa (user_school_roles + role_permissions)."""
from .mock import Opts
from .roles import current_role, nav_for, edit_for, LABELS


def ui(request):
    role = current_role(request)
    return {
        "nav": nav_for(role), "edit": edit_for(role),
        "can": {"create": False, "edit": False, "delete": False},  # sobrescrito por crud_list para cada tela
        "filter_options": Opts(), "user_school_count": 2,
        "role": role, "role_label": LABELS[role], "roles": list(LABELS.items()),
    }