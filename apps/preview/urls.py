"""URLs de PRÉ-VISUALIZAÇÃO. Reaproveita as rotas REAIS de apps/<app>/urls.py (mesmos nomes e namespaces dos templates),
trocando cada view vazia por uma view falsa. Para ligar o backend: em setup/urls.py trocar 'apps.preview.urls' pelos includes reais."""
import importlib, re
from functools import partial
from django.shortcuts import redirect
from django.urls import include, path
from . import views as v

APPS = ["accounts", "access", "schools", "academics", "students", "enrollments", "finance", "privacy", "audit"]
CUSTOM = {"login": v.login, "logout": v.logout, "profile": v.profile, "password_change": v.only_toast, "select_school": v.select_school,
          "permission_matrix": v.permission_matrix, "permission_toggle": v.permission_toggle, "dashboard": v.dashboard,
          "student_record": v.student_record, "new_enrollment": v.new_enrollment, "class_options": v.class_options,
          "guardian_portal": v.guardian_portal, "second_copy": v.second_copy,
          "student_record_enrollments": partial(v.student_partial, kind="m"), "student_record_guardians": partial(v.student_partial, kind="r"),
          "student_record_pickups": partial(v.student_partial, kind="a")}

def build(app):
    out = []
    for p in importlib.import_module("apps.%s.urls" % app).urlpatterns:
        m = re.match(r"^(\w+)_(list|create|edit|delete)$", p.name)
        if m:
            fn = {"list": v.crud_list, "create": v.crud_form, "edit": v.crud_form, "delete": v.crud_delete}[m.group(2)]
            view = partial(fn, app=app, res=m.group(1))
        else:
            view = CUSTOM[p.name]
        out.append(path(str(p.pattern), view, name=p.name))
    return out

urlpatterns = [path("", lambda r: redirect("accounts:login")),
               path("simulacao/perfil/", v.set_role, name="set_role")] + \
              [path("", include((build(a), a))) for a in APPS]