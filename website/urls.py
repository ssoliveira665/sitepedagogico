# from django.urls import path
# from .views import home, eja_cadastro, CustomLoginView, logout_view, logout_confirm, cadastro_usuario, verificar_cpf_ajax, area_do_candidato
# from . import views
# from .views import search_schools_by_address  # Correct function name
# from .views import search_schools_by_cep  # Correct function name
# from .views import get_bairros
# from django.contrib.auth import views as auth_views
# from .views import CustomPasswordResetView ,CustomAdminLoginView # Import your custom view
# from django.shortcuts import redirect

# from .views import listar_funcionarios

# from .views import upload_arquivo

# from .views import verify_cpf_ajax
# from .views import verificar_cpf

# from .views import admin_login_view
# from .views import admin_dashboard

# from .views import regimento_cadastro_view

# class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
#     def get(self, request, *args, **kwargs):
#         return redirect('login')  # Redirect to the login page after password reset


# urlpatterns = [
#     path('', views.home, name='home'),  # Ensure this is your home page
#     path('', views.home, name='pagina_inicial'),  # This is just an example; ensure it matches
#     path('cadastro-eja/', eja_cadastro, name='eja_cadastro'),
#     path('login/', CustomLoginView.as_view(), name='login'),
#     path('cadastro-usuario/', cadastro_usuario, name='cadastro_usuario'),
#     path('verificar_cpf/', views.verificar_cpf_ajax, name='verificar_cpf_ajax'),
#     path('verificar-cpf-ajax/', verificar_cpf_ajax, name='verificar_cpf_ajax'),
#     path('area-candidato/', area_do_candidato, name='area_do_candidato'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('confirmar-logout/', logout_confirm, name='logout_confirm'),  # Página de confirmação de logout
#     path('imprimir-inscricao/<int:inscricao_id>/', views.imprimir_inscricao, name='imprimir_inscricao'),
#     path('imprimir-inscricao/', views.imprimir_inscricao, name='imprimir_inscricao'),
#     path('update-info-pessoal/', views.update_info_pessoal, name='update_info_pessoal'),
#     path('update-inscricao/', views.update_inscricao, name='update_inscricao'),
#     path('update-resultados/', views.update_resultados, name='update_resultados'),
#     path('cadastro/', views.cadastro_candidato, name='cadastro_candidato'),
#     path('search-schools/', search_schools_by_address, name='search_schools_by_address'),
#     path('search-schools/', search_schools_by_cep, name='search_schools_by_cep'),
#     path('bairros/', views.list_bairros, name='list_bairros'),
#     path('search-bairro/', views.search_bairro, name='search_bairro'),
#     path('get-bairros/', get_bairros, name='get_bairros'),
#     path('area-do-candidato/', views.area_do_candidato, name='area_do_candidato'),

#     path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
#     path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), name="password_reset_done"),
#     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"), name="password_reset_confirm"),
#     path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"), name="password_reset_complete"),
#     path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
#     path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
#     path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
#     path('accounts/password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
#     path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
#     path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#     path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
#     path('test-email/', views.test_email),
#     path('listar_funcionarios/', views.listar_funcionarios, name='listar_funcionarios'),
#     path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),

#     path('accounts/login-admin/', CustomAdminLoginView.as_view(), name='login_admin'),
#     path('accounts/login-admin/', CustomAdminLoginView.as_view(), name='admin_login'),  # Add 
#     path('salvar-inscricao/', views.salvar_inscricao_modal, name='salvar_inscricao_modal'),
#     path('editar-inscricao/<int:id>/', views.editar_inscricao, name='editar_inscricao'),
#     path('visualizar-inscricao/<int:id>/', views.visualizar_inscricao, name='visualizar_inscricao'),
#     path('acompanhar-inscricao/<int:id>/', views.acompanhar_inscricao, name='acompanhar_inscricao'),
#     # path('verificar-cpf/', views.verificar_cpf, name='verificar_cpf'),
#     path('verify-cpf/', verify_cpf_ajax, name='cpf_verification'),
#     path('verify-cpf/', views.verify_cpf_ajax, name='verify_cpf_ajax'),
#     path('verify-cpf/', verificar_cpf, name='verify_cpf_ajax'),
#     path('verificar-cpf/', views.verify_cpf_ajax, name='verificar_cpf'),
#     path('admin-login/', admin_login_view, name='admin_login'),

#     path('inscricoes/', views.listar_inscricoes, name='listar_inscricoes'),
#     path('deletar-inscricao/<int:id>/', views.deletar_inscricao, name='deletar_inscricao'),
#     path('editar-inscricao/<int:id>/', views.editar_inscricao, name='editar_inscricao'),
#     path('inativar-inscricao/<int:id>/', views.inativar_inscricao, name='inativar_inscricao'),
#     path('atualizacao/', views.pagina_atualizacao, name='pagina_atualizacao'),

#     path('upload-arquivo/', upload_arquivo, name='upload_arquivo'),

#     path('funcionarios/', listar_funcionarios, name='listar_funcionarios'),

#     path('consulta-publica/', views.consulta_publica, name='consulta_publica'),
#     path('consulta-publica-sucesso/', views.consulta_publica_sucesso, name='consulta_publica_sucesso'),

#     path('cadastro/', regimento_cadastro_view, name='regimento_cadastro'),

# ]


from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.urls import path
from .views import home, eja_cadastro, CustomLoginView, logout_view, logout_confirm, cadastro_usuario, verificar_cpf_ajax, area_do_candidato
from . import views
from .views import search_schools_by_address  # Correct function name
from .views import search_schools_by_cep  # Correct function name
from .views import get_bairros
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView ,CustomAdminLoginView # Import your custom view
from django.shortcuts import redirect

from .views import listar_funcionarios

from .views import upload_arquivo

from .views import verify_cpf_ajax
from .views import verificar_cpf

from .views import admin_login_view
from .views import admin_dashboard

from .views import regimento_cadastro_view

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.home, name='pagina_inicial'),  # This is just an example; ensure it matches
    path('cadastro-eja/', views.eja_cadastro, name='eja_cadastro'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('', include('website.urls')),
    path('cadastro-usuario/', views.cadastro_usuario, name='cadastro_usuario'),
    path('verificar-cpf/', views.verificar_cpf_ajax, name='verificar_cpf_ajax'),
    path('area-candidato/', views.area_do_candidato, name='area_do_candidato'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('confirmar-logout/', views.logout_confirm, name='logout_confirm'),
    
    path('search-schools/address/', views.search_schools_by_address, name='search_schools_by_address'),
    path('search-schools/cep/', views.search_schools_by_cep, name='search_schools_by_cep'),
    path('bairros/', views.list_bairros, name='list_bairros'),
    path('get-bairros/', views.get_bairros, name='get_bairros'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"), name="password_reset_confirm"),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"), name="password_reset_complete"),

    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('login-admin/', views.CustomAdminLoginView.as_view(), name='login_admin'),

    path('listar-funcionarios/', views.listar_funcionarios, name='listar_funcionarios'),
    path('upload-arquivo/', views.upload_arquivo, name='upload_arquivo'),

    path('consulta-publica/', views.consulta_publica, name='consulta_publica'),
    path('cadastro/', views.cadastrar_regimento, name='cadastro_regimento'),
    path('consulta-publica-sucesso/', views.consulta_publica_sucesso, name='consulta_publica_sucesso'),
    path('listar/', views.listar_registros, name='listar_registros'),
    path('sucesso/', views.consulta_publica_sucesso, name='sucesso'),

    # CPF verification
    path('verify-cpf/', views.verify_cpf_ajax, name='verify_cpf_ajax'),

    # Inscription management
    path('inscricoes/', views.listar_inscricoes, name='listar_inscricoes'),
    path('editar-inscricao/<int:id>/', views.editar_inscricao, name='editar_inscricao'),
    path('visualizar-inscricao/<int:id>/', views.visualizar_inscricao, name='visualizar_inscricao'),
    path('inativar-inscricao/<int:id>/', views.inativar_inscricao, name='inativar_inscricao'),

    path('test-email/', views.test_email, name='test_email'),

    path('admin-login/', admin_login_view, name='admin_login'),

# Exibe o formulário de edição ou visualização de um regimento específico
    path('regimento/<int:pk>/', views.regimento_form_view, name='regimento_form'),

    # Exibe a lista de todos os regimentos cadastrados
    path('regimentos/', views.regimento_list_view, name='regimento_list'),

    # Exibe a lista de registros (pode ser uma rota alternativa ou removida)
    # Se esta rota é redundante, você pode removê-la
    path('registros/', views.listar_registros, name='listar_registros'),

    # Alguma outra view específica
    path('some-path/', views.some_view, name='some_view'),

    path('exportar/csv/', views.exportar_csv, name='exportar_csv'),
    path('exportar/excel/', views.exportar_excel, name='exportar_excel'),
    path('exportar/pdf/', views.exportar_pdf, name='exportar_pdf'),
]


