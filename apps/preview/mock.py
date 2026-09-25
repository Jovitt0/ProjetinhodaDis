"""DADOS FALSOS só para pré-visualizar as telas. Nada aqui vai para produção: apagar apps/preview quando o backend real entrar."""
import datetime, json, re, uuid
from pathlib import Path
from django.template.loader import get_template
from django.utils.safestring import mark_safe

SCREENS = json.loads((Path(__file__).parent / "screens.json").read_text(encoding="utf-8"))  # gerado junto com os templates

class M(dict):
    """dict com acesso por ponto. O template do Django já lê dict[chave] quando você escreve {{ obj.chave }}."""
    def __getattr__(self, k):
        if k.startswith("__"): raise AttributeError(k)
        return self.get(k)

class AllTrue(dict):          # nav.qualquer_coisa e can.qualquer_coisa → sempre True
    def __missing__(self, k): return True
class Opts(dict):             # filter_options.qualquer_filtro → duas opções de exemplo
    def __missing__(self, k): return [("1", "Opção 1"), ("2", "Opção 2")]
class Page(list):             # imita o page_obj do Paginator (uma página só)
    paginator = M(num_pages=1)
    number = 1
class Form(list):             # imita um formulário: iterável de campos
    non_field_errors = []

LABELS = {"full_name": "Nome completo", "email": "E-mail", "status": "Situação", "name": "Nome", "code": "Código", "description": "Descrição",
          "password": "Senha", "student": "Aluno", "course": "Curso", "class_group": "Turma", "academic_year": "Ano letivo", "teacher": "Professor",
          "subject": "Disciplina", "birth_date": "Data de nascimento", "phone": "Telefone", "document_number": "Documento", "notes": "Observações"}
SELECTS = {"status", "course", "academic_year", "class_group", "subject", "teacher", "student", "user", "roles", "retention_rule", "enrollment",
           "responsible", "contribution_plan", "frequency", "severity", "request_type", "legal_basis", "disposal_action", "timezone", "relationship_type"}

class F:
    """Campo de formulário falso: tem o que o components/_field.html usa (label, errors, id_for_label, help_text) e imprime um <input>."""
    errors, help_text = [], ""
    def __init__(self, name, label=None):
        self.name, self.label, self.id_for_label = name, label or LABELS.get(name, name.replace("_", " ").capitalize()), "id_" + name
    def __str__(self):
        n, i = self.name, "id_" + self.name
        if n in ("description", "notes", "purpose", "data_categories"): h = '<textarea id="%s" name="%s" rows="3"></textarea>' % (i, n)
        elif n in SELECTS: h = '<select id="%s" name="%s"><option value="">Selecione</option><option>Opção 1</option><option>Opção 2</option></select>' % (i, n)
        elif n.startswith("is_") or n == "active": h = '<input id="%s" type="checkbox" name="%s" style="width:auto">' % (i, n)
        else:
            t = "password" if "password" in n else "email" if n == "email" else "number" if n in ("year", "amount", "retention_days") else \
                "datetime-local" if n.endswith("_at") else "date" if n.endswith(("_on", "_date", "_from", "_until")) else "text"
            h = '<input id="%s" type="%s" name="%s">' % (i, t, n)
        return mark_safe(h)
    __html__ = __str__

PEOPLE = ["Ana Beatriz Lima", "Carlos Eduardo Souza", "Fernanda Oliveira", "João Pedro Santos", "Mariana Costa", "Rafael Almeida", "Luciana Pereira", "Thiago Ribeiro"]
DISPLAY = ["Ativa", "Pendente", "Inativa"]
_cur = ["Ensino Fundamental I", "Ensino Fundamental II", "Ensino Médio"]; _sub = ["Matemática", "Língua Portuguesa", "Ciências", "História"]
_cls = ["5º A", "5º B", "6º A", "7º C"]; _yr = ["Ano letivo 2026", "Ano letivo 2025"]; _ret = ["Prontuário — 5 anos", "Financeiro — 10 anos"]
NAMES = {"courses": _cur, "course": _cur, "subjects": _sub, "subject": _sub, "classes": _cls, "class_group": _cls, "academic_years": _yr, "academic_year": _yr,
         "plans": ["Mensalidade integral", "Mensalidade parcial", "Taxa de material"], "activities": ["Cadastro de alunos", "Controle de acesso", "Comunicação com responsáveis"],
         "retention_rule": _ret, "retention": _ret, "schools": ["E.M. Paulo Freire", "E.E. Cecília Meireles", "EMEB Monteiro Lobato"],
         "incidents": ["Acesso indevido a planilha", "Perda de notebook", "E-mail enviado ao destinatário errado"]}
EXACT = {"request_type": ["Acesso", "Correção", "Eliminação"], "severity": ["Baixa", "Média", "Alta"], "frequency": ["Mensal"], "legal_basis": ["Obrigação legal", "Política pública"],
         "disposal_action": ["Anonimizar", "Excluir"], "entity_type": ["students", "payments"], "retention_days": [1825, 3650], "grade_level": ["5º ano", "6º ano"],
         "status": DISPLAY, "relationship_type": ["Mãe", "Pai", "Avó"], "external_reference": ["BOL-1001", "BOL-1002"]}

def leaf(parts, i, res):
    """Valor de exemplo para o campo (último item do caminho), escolhido pelo nome do campo."""
    n = parts[-1]; parent = parts[-2] if len(parts) > 1 else res
    if n in EXACT: return EXACT[n][i % len(EXACT[n])]
    if n in ("name", "title") and parent in NAMES: return NAMES[parent][i % len(NAMES[parent])]
    if n in ("full_name", "requester_name", "authorized_name"): return PEOPLE[(i + len(parts)) % len(PEOPLE)]
    if n.startswith("get_") and n.endswith("_display"): return DISPLAY[i % 3]
    if n == "amount_display": return "R$ %d,00" % (250 + 50 * i)
    if n == "year": return 2026 - i % 2
    if n.endswith("_at"): return datetime.datetime(2026, 9, i + 1, 9, 30)
    if n.endswith(("_on", "_from", "_until", "_date")): return datetime.date(2026, 3, i + 1)
    if n.startswith("is_") or n == "active": return i % 3 != 2
    if n == "email": return "contato%d@escola.gov.br" % (i + 1)
    if n == "code": return "C%03d" % (i + 1)
    if n in ("registration_number", "enrollment_number"): return "ESC01-2026-%06d" % (100 + i)
    if n in ("document_number", "requester_document"): return "123.456.789-%02d" % i
    if n == "phone": return "(48) 99999-%04d" % i
    if n == "ip_address": return "200.10.20.%d" % (10 + i)
    if n == "purpose": return "Finalidade de exemplo para o tratamento de dados %d" % (i + 1)
    if n == "description": return "Mensalidade %02d/2026" % (i % 12 + 1)
    return "%s %d" % (n.replace("_", " ").capitalize(), i + 1)

def build(paths, i, res):
    """Monta 1 objeto falso com exatamente os campos que a tabela usa (lidos do próprio template)."""
    o = M(pk=str(uuid.UUID(int=i + 1)))
    for p in paths:
        parts = p.split(".")
        if parts[-1] == "all":       # ex.: obj.roles.all
            o[parts[0]] = M(all=[M(name="Secretaria"), M(name="Financeiro")]); continue
        d = o
        for k in parts[:-1]: d = d.setdefault(k, M())
        d.setdefault(parts[-1], leaf(parts, i, res))
    return o

def make_rows(app, res):
    src = get_template("%s/partials/%s_table.html" % (app, res)).template.source
    paths = sorted({p.rstrip(".") for p in re.findall(r"obj\.([A-Za-z_][\w.]*)", src)} - {"pk"})
    return [build(paths, i, res) for i in range(8)]
