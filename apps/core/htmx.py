"""Helpers HTMX compartilhados. Requer 'django_htmx' (INSTALLED_APPS + HtmxMiddleware) para request.htmx."""
import json
from django.http import HttpResponse

def htmx_saved(message="Salvo com sucesso"):
    """Resposta padrão de sucesso de um modal: 204 (sem swap) + eventos que fecham o modal,
    recarregam #tabela e mostram o toast. O front escuta esses nomes em static/js/app.js."""
    resp = HttpResponse(status=204)
    resp["HX-Trigger"] = json.dumps({"modal-fechar": True, "tabela-atualizar": True, "toast": {"msg": message}})
    return resp

def htmx_deleted():
    """hx-delete: 200 com corpo vazio remove a linha (hx-swap=outerHTML) + atualiza a tabela."""
    resp = HttpResponse("", status=200)
    resp["HX-Trigger"] = json.dumps({"toast": {"msg": "Registro excluído"}})
    return resp
