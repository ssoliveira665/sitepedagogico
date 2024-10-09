from django.urls import path
from .views import home, eja_cadastro, CustomLoginView, logout_view, logout_confirm, cadastro_usuario, verificar_cpf_ajax, area_do_candidato
from . import views
from .views import search_schools_by_address  # Correct function name
from .views import search_schools_by_cep  # Correct function name
from .views import get_bairros
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView ,CustomAdminLoginView # Import your custom view
from django.shortcuts import redirect

from .views import admin_dashboard_view

class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
    def get(self, request, *args, **kwargs):
        return redirect('login')  # Redirect to the login page after password reset


urlpatterns = [
    path('', views.home, name='home'),  # Ensure this is your home page
    path('', views.home, name='pagina_inicial'),  # This is just an example; ensure it matches
    path('cadastro-eja/', eja_cadastro, name='eja_cadastro'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('cadastro-usuario/', cadastro_usuario, name='cadastro_usuario'),
    path('verificar_cpf/', views.verificar_cpf_ajax, name='verificar_cpf_ajax'),
    path('verificar-cpf-ajax/', verificar_cpf_ajax, name='verificar_cpf_ajax'),
    path('area-candidato/', area_do_candidato, name='area_do_candidato'),
    path('logout/', logout_view, name='logout'),  # URL de logout via POST
    path('confirmar-logout/', logout_confirm, name='logout_confirm'),  # Página de confirmação de logout
    path('imprimir-inscricao/<int:inscricao_id>/', views.imprimir_inscricao, name='imprimir_inscricao'),
    path('imprimir-inscricao/', views.imprimir_inscricao, name='imprimir_inscricao'),
    path('update-info-pessoal/', views.update_info_pessoal, name='update_info_pessoal'),
    path('update-inscricao/', views.update_inscricao, name='update_inscricao'),
    path('update-resultados/', views.update_resultados, name='update_resultados'),
    path('cadastro/', views.cadastro_candidato, name='cadastro_candidato'),
    path('search-schools/', search_schools_by_address, name='search_schools_by_address'),
    path('search-schools/', search_schools_by_cep, name='search_schools_by_cep'),
    path('bairros/', views.list_bairros, name='list_bairros'),
    path('search-bairro/', views.search_bairro, name='search_bairro'),
    path('get-bairros/', get_bairros, name='get_bairros'),
    path('area-do-candidato/', views.area_do_candidato, name='area_do_candidato'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"), name="password_reset_complete"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('accounts/password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('test-email/', views.test_email),
    path('admin/dashboard/', admin_dashboard_view, name='admin_dashboard'),

    path('accounts/login-admin/', CustomAdminLoginView.as_view(), name='login_admin'),
    path('accounts/login-admin/', CustomAdminLoginView.as_view(), name='admin_login'),  # Add 
    path('salvar-inscricao/', views.salvar_inscricao_modal, name='salvar_inscricao_modal'),
    path('editar-inscricao/<int:id>/', views.editar_inscricao, name='editar_inscricao'),
    path('visualizar-inscricao/<int:id>/', views.visualizar_inscricao, name='visualizar_inscricao'),
    path('acompanhar-inscricao/<int:id>/', views.acompanhar_inscricao, name='acompanhar_inscricao'),

]
