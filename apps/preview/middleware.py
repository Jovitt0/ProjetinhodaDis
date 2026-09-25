"""Simula usuário logado e escola ativa, e lê o perfil escolhido no seletor do topo (guardado na sessão).
No backend real: AuthenticationMiddleware + ActiveSchoolMiddleware — sem seletor manual de perfil."""
from .mock import M
from .roles import current_role


class PreviewUserMiddleware:
    def __init__(self, get_response): self.get_response = get_response

    def __call__(self, request):
        role = current_role(request)
        request.user = M(full_name="Maria Souza (simulação)", email="maria@escola.gov.br", is_authenticated=True)
        request.active_school = M(name="Todas as escolas (visão global)", code="—") if role == "master" \
            else M(name="E.M. Paulo Freire", code="ESC01")
        return self.get_response(request)