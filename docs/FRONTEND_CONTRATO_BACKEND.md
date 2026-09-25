# Contrato front-end ⇄ backend (Django + HTMX)

## Regras
1. **Nunca** há `school_id` em formulário/URL: o backend usa `request.active_school` (ActiveSchoolMiddleware).
2. Listagens: `request.htmx` → devolver só `<app>/partials/<recurso>_table.html`; senão a página inteira.
3. Modal (novo/editar): `GET` → `components/_crud_form.html` com `form`, `form_title`, `action_url`. `POST` válido → `htmx_saved()` (apps/core/htmx.py). Inválido → mesmo template com **status 422**.
4. Exclusão: `hx-delete` → `htmx_deleted()`.
5. Contexto global (context processor): `nav` = `{schools, academics, students, enrollments, finance, privacy, access, audit: bool}`, `can` = `{create, edit, delete: bool}` para o recurso atual, `user_school_count`.
6. Propriedades esperadas nos models: `amount_display` (R$ a partir de `amount_cents`), `class_group` (FK da tabela `classes`), `roles` em `user_school_links`.
7. Ícone de estado/rótulos usam `get_<campo>_display`.

## Setup rápido
```python
# settings: INSTALLED_APPS += ["django_htmx"]; MIDDLEWARE += ["django_htmx.middleware.HtmxMiddleware"]
# TEMPLATES[0]["DIRS"] = [BASE_DIR / "templates"]; STATICFILES_DIRS = [BASE_DIR / "static"]
# config/urls.py: path("", include("apps.schools.urls")) ... um include por app (namespaces = nome do app)
```

## Mapa das telas
| Tela | URL name | Template | Tabelas | Campos do form / contexto |
|---|---|---|---|---|
| 3 | `accounts:profile` | `accounts/profile.html` | users | user_form (full_name, email), password_form (old_password, new_password1, new_password2) |
| 4 | `access:users_list` | `access/user_management.html` | users, user_school_links | full_name, email, status (+ formset de vínculos com escolas) |
| 5 | `access:memberships_list` | `access/roles_management.html` | user_school_roles, roles | roles (múltipla escolha), status |
| 6 | `access:permission_matrix` | `access/permission_matrix.html` | permissions, role_permissions | roles (lista), matrix {recurso: [{permission, cells: [{role, granted}]}]}; só Admin Global |
| 7 | `schools:schools_list` | `schools/school_list.html` | schools | code, name, legal_name, document_number, status, timezone |
| 8 | `schools:academic_years_list` | `schools/academic_years.html` | academic_years | year, name, starts_on, ends_on, status |
| 9 | `schools:dashboard` | `schools/dashboard.html` | enrollments, classes, payments (agregados da escola ativa) | metrics {enrolled, active_classes, overdue_payments, overdue_amount_display} |
| 10 | `academics:courses_list` | `academics/course_list.html` | courses | code, name, description, status |
| 11 | `academics:subjects_list` | `academics/subject_list.html` | subjects | course, code, name, description, status |
| 12 | `academics:classes_list` | `academics/class_list.html` | classes | course, academic_year, code, name, grade_level |
| 13 | `academics:teachers_list` | `academics/teacher_list.html` | teachers | full_name, registration_number, document_number, user (opcional) |
| 14 | `academics:assignments_list` | `academics/teacher_assignments.html` | teacher_class_assignments | teacher, class_group, subject, starts_on, ends_on, is_primary |
| 15 | `students:students_list` | `students/student_list.html` | students | registration_number, full_name, social_name, birth_date, document_number, status |
| 16 | `students:responsibles_list` | `students/responsible_list.html` | responsibles, student_responsibles | full_name, document_number, email, phone (+ formset student_responsibles: student, relationship_type, is_primary) |
| 17 | `students:pickups_list` | `students/pickup_authorizations.html` | student_pickup_authorizations | student, authorized_name, document_number, relationship_type, valid_from, valid_until, is_active, notes |
| 18 | `students:student_record` | `students/student_record.html` | students, enrollments, student_responsibles, student_pickup_authorizations | student, secoes = [(id, título, url_name)] para as parciais student_record_enrollments/_guardians/_pickups (carregadas via HTMX) |
| 19 | `enrollments:new_enrollment` | `enrollments/new_enrollment.html` | enrollments, enrollment_sequences | form (student, academic_year, class_group); POST cria matrícula — o número (CODIGO-ESCOLA-ANO-SEQUENCIA) é gerado pelo banco |
| 20 | `enrollments:enrollments_list` | `enrollments/enrollment_dashboard.html` | enrollments | status (edição); criação é feita na Tela 19 |
| 21 | `finance:plans_list` | `finance/contribution_plans.html` | contribution_plans | name, description, amount (reais → amount_cents), frequency, active |
| 22 | `finance:payments_list` | `finance/payment_management.html` | payments | enrollment, responsible, contribution_plan, description, due_date, amount, status, paid_at, external_reference |
| 23 | `finance:guardian_portal` | `finance/guardian_portal.html` | payments (do responsável logado) | payments (pendentes e pagos do responsável), can_second_copy |
| 24 | `privacy:activities_list` | `privacy/processing_activities.html` | processing_activities | name, purpose, legal_basis, data_categories (JSON), retention_rule, active |
| 25 | `privacy:retention_list` | `privacy/retention_rules.html` | retention_rules | name, entity_type, retention_days, disposal_action, active |
| 26 | `privacy:dsar_list` | `privacy/dsar_requests.html` | data_subject_requests | requester_name, requester_document, request_type, description, status, completed_at |
| 27 | `privacy:incidents_list` | `privacy/security_incidents.html` | security_incidents | title, description, severity, occurred_at, resolved_at, status |
| 28 | `audit:logs_list` | `audit/audit_logs.html` | audit_logs (somente leitura) | — (tela imutável) |
| 1 | `accounts:login` | `accounts/login.html` | users | form(email, password) |
| 2 | `access:select_school` | `access/select_school.html` | user_school_links | memberships; POST `membership_id` |
