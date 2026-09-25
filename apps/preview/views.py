"""Views FALSAS: renderizam os templates reais com dados de exemplo. Nada é gravado em banco."""
import datetime, json, uuid
from django.http import HttpResponse
from django.shortcuts import redirect, render
from apps.core.htmx import htmx_saved, htmx_deleted
from .mock import M, F, Form, Page, SCREENS, PEOPLE, make_rows
from .roles import can_for, current_role, LABELS

def toast(msg):  # 204 + aviso na tela (o front escuta o evento 'toast')
    r = HttpResponse(status=204); r["HX-Trigger"] = json.dumps({"toast": {"msg": msg}}); return r
_id = lambda i: str(uuid.UUID(int=i))

# ---- Telas de listagem (CRUD) ----
def crud_list(request, app, res):
    s = SCREENS[app + "/" + res]
    rows = make_rows(app, res)
    q = request.GET.get("q", "").lower()
    if q: rows = [r for r in rows if q in str(r).lower()]
    # HTMX pede só a tabela (parcial); acesso direto pelo navegador recebe a página completa
    tpl = (app + "/partials/" + res + "_table.html") if request.headers.get("HX-Request") else (app + "/" + s["tpl"] + ".html")
    ctx = {"page_obj": Page(rows), "can": can_for(current_role(request), res)}
    return render(request, tpl, ctx)

def crud_form(request, app, res, pk=None):
    if request.method == "POST": return htmx_saved("Salvo (simulação: nada foi gravado)")
    s = SCREENS[app + "/" + res]
    return render(request, "components/_crud_form.html", {"form": Form(F(n) for n in s["fields"]),
                  "form_title": ("Editar — " if pk else "Novo cadastro — ") + s["title"], "action_url": request.path})

def crud_delete(request, app, res, pk): return htmx_deleted()

# ---- Telas 1, 2, 3 ----
def login(request):
    if request.method == "POST": return redirect("access:select_school")
    return render(request, "accounts/login.html", {"form": M(email=F("email"), password=F("password"), non_field_errors=[]), "next": ""})
def logout(request): return redirect("accounts:login")
def select_school(request):
    if request.method == "POST": return redirect("schools:dashboard")
    ms = [M(pk=_id(i + 1), school=M(name=n), roles=M(all=[M(name=r)])) for i, (n, r) in enumerate([("E.M. Paulo Freire", "Secretaria"), ("E.E. Cecília Meireles", "Administrador da escola")])]
    return render(request, "access/select_school.html", {"memberships": ms})
def profile(request):
    if request.method == "POST": return toast("Dados salvos (simulação)")
    return render(request, "accounts/profile.html", {"user_form": Form([F("full_name"), F("email")]),
                  "password_form": Form([F("old_password", "Senha atual"), F("new_password1", "Nova senha"), F("new_password2", "Confirmar nova senha")])})
def only_toast(request): return toast("Salvo (simulação)")

def set_role(request):
    """Seletor de perfil do topo — troca o papel simulado na sessão. Não existe no backend real (o perfil vem do vínculo do usuário)."""
    if request.method == "POST":
        request.session["preview_role"] = request.POST.get("role", "master")
    nxt = request.POST.get("next") or request.META.get("HTTP_REFERER")
    return redirect(nxt) if nxt else redirect("schools:dashboard")

# ---- Tela 6 ----
ROLES = [M(pk=str(i), name=n) for i, n in enumerate(["Administrador da escola", "Secretaria", "Financeiro", "Professor"])]
def permission_matrix(request):
    acoes = ["Visualizar", "Criar", "Editar", "Excluir"]
    matrix = {rec: [M(permission=M(pk=rec + a, name=a), cells=[M(role=r, granted=(j + k) % 2 == 0) for k, r in enumerate(ROLES)]) for j, a in enumerate(acoes)]
              for rec in ("Alunos", "Matrículas", "Cobranças")}
    return render(request, "access/permission_matrix.html", {"roles": ROLES, "matrix": matrix})
def permission_toggle(request): return HttpResponse(status=204)

# ---- Tela 9 ----
def dashboard(request):
    role = current_role(request)
    if role == "master":
        schools = [M(name=n, code=c, students=s, classes=k, overdue=o) for n, c, s, k, o in [
            ("E.M. Paulo Freire", "ESC01", 482, 21, 37), ("E.E. Cecília Meireles", "ESC02", 301, 14, 12),
            ("EMEB Monteiro Lobato", "ESC03", 198, 9, 5)]]
        return render(request, "schools/master_dashboard.html", {"schools": schools,
            "totals": M(students=sum(s.students for s in schools), classes=sum(s.classes for s in schools))})
    if role == "professor":
        classes = [M(name=n, students=q, subject=s) for n, q, s in [("6º A", 28, "Matemática"), ("7º C", 25, "Matemática")]]
        return render(request, "academics/teacher_dashboard.html", {"classes": classes})
    recent = [M(student=PEOPLE[i % len(PEOPLE)], class_group="6º A", enrolled_at=datetime.date(2026, 9, i + 1)) for i in range(5)]
    return render(request, "schools/dashboard.html", {"metrics": M(enrolled=482, active_classes=21, teachers=34,
        overdue_payments=37, overdue_amount_display="R$ 12.940,00", confirmed_amount_display="R$ 58.420,00"),
        "recent_enrollments": recent, "can_new_student": can_for(role, "students")["create"]})

# ---- Tela 18 ----
def student_record(request, pk):
    secoes = [("m", "Matrículas", "students:student_record_enrollments"), ("r", "Responsáveis", "students:student_record_guardians"), ("a", "Autorizações de retirada", "students:student_record_pickups")]
    return render(request, "students/student_record.html", {"student": M(pk=pk, full_name=PEOPLE[0], registration_number="2026-000123"), "secoes": secoes})
def student_partial(request, pk, kind):
    html = {"m": "<ul><li>2026 — 5º A — Ativa (ESC01-2026-000123)</li><li>2025 — 4º B — Concluída</li></ul>",
            "r": "<ul><li>Fernanda Oliveira — Mãe (principal)</li><li>Carlos Souza — Pai</li></ul>",
            "a": "<ul><li>Luciana Pereira — Tia — válida até 31/12/2026</li></ul>"}[kind]
    return HttpResponse(html)

# ---- Tela 19 ----
def new_enrollment(request):
    if request.method == "POST": return toast("Matrícula ESC01-2026-000483 criada (simulação)")
    anos = [M(pk="1", name="Ano letivo 2026"), M(pk="2", name="Ano letivo 2025")]
    return render(request, "enrollments/new_enrollment.html", {"form": M(student=F("student"), class_group=F("class_group"), academic_year=M(field=M(queryset=anos)))})
def class_options(request): return render(request, "components/_field.html", {"field": F("class_group")})

# ---- Tela 23 ----
def guardian_portal(request):
    pays = [M(pk=_id(1), description="Mensalidade 08/2026", due_date=datetime.date(2026, 8, 10), amount_display="R$ 350,00", status="overdue", get_status_display="Em atraso"),
            M(pk=_id(2), description="Mensalidade 09/2026", due_date=datetime.date(2026, 9, 10), amount_display="R$ 350,00", status="pending", get_status_display="Pendente"),
            M(pk=_id(3), description="Mensalidade 07/2026", due_date=datetime.date(2026, 7, 10), amount_display="R$ 350,00", status="paid", get_status_display="Pago")]
    return render(request, "finance/guardian_portal.html", {"payments": pays})
def second_copy(request, pk): return HttpResponse("Segunda via da cobrança (simulação)")