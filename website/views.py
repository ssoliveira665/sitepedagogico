from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Inscricao
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate  # Para logar o usuário automaticamente após o cadastro
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views.decorators.http import require_POST
from datetime import datetime
from django.core.exceptions import ValidationError
from decimal import Decimal
import base64
from django.template.loader import render_to_string  # Certifique-se de importar render_to_string

from io import BytesIO
from django.http import HttpResponse
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from .forms import CandidatoForm

from weasyprint import HTML
import qrcode
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

from .models import School
from .models import Bairro
from .models import Disciplina

from .forms import CPFLoginForm

from django.contrib.auth import views as auth_views

from django.core.mail import send_mail

import csv




def cadastro_candidato(request):
    if request.method == 'POST':
        form = CandidatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Replace with your success page
    else:
        form = CandidatoForm()
    
    return render(request, 'cadastro_candidato.html', {'form': form})
#**********************************************************************************************************

def home(request):
    return render(request, 'home.html')
#**********************************************************************************************************

def eja_cadastro(request):
    return render(request, 'cadastro_eja.html')
#**********************************************************************************************************

# Exemplo de uma view de login personalizada
def custom_login(request):
    return render(request, 'login.html')
#**********************************************************************************************************

def verificar_cpf(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        try:
            # Tenta encontrar o usuário pelo CPF
            usuario = Usuario.objects.get(cpf=cpf)
            # Se encontrar o CPF, redireciona para a página de perfil ou página de boas-vindas
            return redirect('pagina_inicial')
        except Usuario.DoesNotExist:
            # Se o CPF não existir, redireciona para a página de cadastro
            return redirect('cadastro_usuario')
    return render(request, 'verificar_cpf.html')  # Página que exibe o modal para inserir CPF
#**********************************************************************************************************

def verificar_cpf_ajax(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        print(f"Recebido CPF: {cpf}")  # Log para verificar o CPF

        if not cpf:
            print("CPF não fornecido ou inválido")
            return JsonResponse({'status': 'erro', 'message': 'CPF inválido'})

        try:
            # Verifica se o CPF existe no banco de dados
            usuario = Usuario.objects.get(cpf=cpf)
            print("CPF encontrado")  # Loga se o CPF foi encontrado
            return JsonResponse({'status': 'existe'})
        except Usuario.DoesNotExist:
            print("CPF não encontrado")  # Loga se o CPF não foi encontrado
            return JsonResponse({'status': 'nao_existe'})
    
    # Loga se o método não for POST
    print("Método inválido")
    return JsonResponse({'status': 'erro', 'message': 'Requisição inválida'})
#**********************************************************************************************************

def cadastro_usuario(request):
    if request.method == 'POST':
        # Fetching user fields
        nome_completo = request.POST.get('nome_completo')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        # Handle CPF duplication error
        if Usuario.objects.filter(cpf=cpf).exists():
            return render(request, 'error_page.html', {'cpf_error': f"Este CPF ({cpf}) já está cadastrado."})

        # Handle password mismatch error
        if senha != confirmar_senha:
            return render(request, 'error_page.html', {'password_error': "As senhas não coincidem."})


        data_nascimento = request.POST.get('data_nascimento')

        # Additional fields for Inscricao
        responsavel_legal = request.POST.get('nome_responsavel')
        tipo_responsavel = request.POST.get('tipo_responsavel')
        telefone = request.POST.get('telefone')
        telefone_secundario = request.POST.get('telefone_2')
        endereco = request.POST.get('endereco')
        bairro = request.POST.get('bairro')
        ponto_referencia = request.POST.get('ponto_referencia')
        possui_necessidade_especial = request.POST.get('possui_necessidade_especial')
        tipo_necessidade_especial = request.POST.get('necessidade_especial_detalhe')
        turno_disponivel = request.POST.get('turno_disponivel')
        etapa_pretendida = request.POST.get('etapa_pretendida')
        prova_todas_disciplinas = request.POST.get('prova_todas_disciplinas')

        # Verifying passwords
        if senha != confirmar_senha:
            messages.error(request, "As senhas não coincidem!")
            return render(request, 'cadastro_usuario.html')

        # Check if CPF already exists
        if Usuario.objects.filter(cpf=cpf).exists():
            messages.error(request, "Este CPF já está cadastrado.")
            return render(request, 'cadastro_usuario.html')

        try:
            # Create user with encrypted password
            usuario = Usuario.objects.create_user(
                username=email,
                nome_completo=nome_completo,
                cpf=cpf,
                email=email,
                password=senha,
                data_nascimento=data_nascimento,
            )

            # Create the corresponding Inscricao and store it in a variable
            inscricao = Inscricao.objects.create(
                candidato=usuario,
                responsavel_legal=responsavel_legal,
                tipo_responsavel=tipo_responsavel,
                telefone=telefone,
                telefone_secundario=telefone_secundario,
                endereco=endereco,
                bairro=bairro,
                ponto_referencia=ponto_referencia,
                necessidade_especial=(possui_necessidade_especial == 'Sim'),
                tipo_necessidade_especial=tipo_necessidade_especial,
                turno_disponivel=turno_disponivel,
                etapa_pretendida=etapa_pretendida,
                prova_todas_disciplinas=prova_todas_disciplinas
            )

            # Handle disciplines
            if prova_todas_disciplinas == 'Sim':
                # If all disciplines, add all to inscricao
                all_disciplinas = Disciplina.objects.all()
                inscricao.disciplinas.set(all_disciplinas)
            else:
                # If 'Não', only add selected disciplines
                selected_disciplinas = request.POST.getlist('disciplinas')
                inscricao.disciplinas.set(selected_disciplinas)

            # Log the user in and redirect to the candidate area
            login(request, usuario)
            return redirect('area_do_candidato')

        except ValidationError as e:
            # Handle any validation error (e.g., incorrect data)
            messages.error(request, str(e))
            return render(request, 'cadastro_usuario.html')

    # Render the registration page if not a POST request
    return render(request, 'cadastro_usuario.html')
#**********************************************************************************************************

@login_required
def area_do_candidato(request):
    inscricao = Inscricao.objects.filter(candidato=request.user).first()
    
    if not inscricao:
        # Handle case when no inscricao is found
        messages.warning(request, "Nenhuma inscrição encontrada.")
    
    return render(request, 'area_do_candidato.html', {'inscricao': inscricao})
#**********************************************************************************************************

def imprimir_inscricao(request, inscricao_id):
    # Recupera a inscrição
    inscricao = get_object_or_404(Inscricao, id=inscricao_id)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="inscricao.pdf"'

    # Cria um buffer para armazenar o PDF
    buffer = BytesIO()

    # Cria um PDF com tamanho de página A4
    pdf = canvas.Canvas(buffer, pagesize=A4)
    pdf.setTitle(f"Inscrição {inscricao_id}")

    # Definindo margens e coordenadas iniciais
    width, height = A4
    margin = 50

    # Cabeçalho com logo da secretaria e título centralizado
    logo_path = 'C:\\Users\\sysco\\Desktop\\siteDiagnosis\\websys\\static\\img\\logoEsquerda.png'
    if logo_path:
        pdf.drawImage(logo_path, margin, height - 95, width=80, height=80)
    
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawCentredString(width / 2.0, height - 110, "Secretaria Municipal de Educação - Canaã dos Carajás")

    # Subtítulo
    pdf.setFont("Helvetica", 14)
    pdf.drawCentredString(width / 2.0, height - 130, f"Ficha de Inscrição no EJA - Nº {inscricao_id}")

    # Espaçamento antes das tabelas
    pdf.setFont("Helvetica", 12)

    # Ajuste: Verifica se 'data_nascimento' existe antes de usar strftime
    data_nascimento = inscricao.candidato.data_nascimento.strftime('%d/%m/%Y') if inscricao.candidato.data_nascimento else "Data não informada"

    # --- Tabela de Dados Pessoais ---
    dados_pessoais = [
        ["Nome Completo:", inscricao.candidato.nome_completo],
        ["E-Mail:", inscricao.candidato.email],
        ["CPF:", inscricao.candidato.cpf],
        ["Data de Nascimento:", data_nascimento],
        ["Candidato é maior de 18 anos?", 'Sim' if Usuario.maior_de_18 else 'Não'],
        ["Nome do Responsável Legal:", inscricao.responsavel_legal],
        ["Tipo de Responsável Legal:", inscricao.tipo_responsavel],
        ["Telefone Principal:", inscricao.telefone],
        ["Telefone Secundário:", inscricao.telefone_secundario],
        ["Possui Necessidade Especial?", 'Sim' if inscricao.necessidade_especial else 'Não'],  
        ["Tipo de Necessidade Especial:", inscricao.tipo_necessidade_especial if inscricao.necessidade_especial else 'N/A'],
        ["Etapa Pretendida para Matrícula:", inscricao.etapa_pretendida]  # New field
    ]
    personal_table = Table(dados_pessoais, colWidths=[200, 300])
    personal_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.whitesmoke, colors.lightgrey])
    ]))

    # --- Tabela de Dados de Necessidades Especiais ---
    dados_needs = [
        ["Possui Necessidades Especiais?", 'Sim' if inscricao.necessidade_especial else 'Não'],
        ["Necessidades Especiais:", inscricao.tipo_necessidade_especial if inscricao.necessidade_especial else 'N/A'],
        ["Turno Disponível para Estudo:", inscricao.turno_disponivel],
        ["Etapa Pretendida para Matrícula:", inscricao.etapa_pretendida]
    ]
    needs_table = Table(dados_needs, colWidths=[200, 300])
    needs_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.whitesmoke, colors.lightgrey])
    ]))

    # --- Tabela de Endereço ---
    dados_endereco = [
        ["Endereço:", inscricao.endereco],
        ["Bairro:", inscricao.bairro],
        ["Ponto de Referência:", inscricao.ponto_referencia]
    ]
    endereco_table = Table(dados_endereco, colWidths=[200, 300])
    endereco_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.whitesmoke, colors.lightgrey])
    ]))

    # Desenha as tabelas no PDF
    personal_table.wrapOn(pdf, width, height)
    personal_table.drawOn(pdf, margin, height - 370)
    
    needs_table.wrapOn(pdf, width, height)
    needs_table.drawOn(pdf, margin, height - 470)

    endereco_table.wrapOn(pdf, width, height)
    endereco_table.drawOn(pdf, margin, height - 550)

    # Gerar o QR Code e salvá-lo no buffer de memória
    qr_code_img = qrcode.make(f"Inscrição {inscricao_id}")
    qr_buffer = BytesIO()
    qr_code_img.save(qr_buffer, format='PNG')
    qr_buffer.seek(0)

    # Usa ImageReader do reportlab para carregar a imagem do QR Code
    qr_image = ImageReader(qr_buffer)
    pdf.drawImage(qr_image, width - 130, margin - 40, width=100, height=100)

    # Finaliza o PDF
    pdf.showPage()
    pdf.save()

    # Retorna o PDF como resposta HTTP
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')

#**********************************************************************************************************

class CustomLoginView(LoginView):
    template_name = 'login.html'  # Nome do template
    redirect_authenticated_user = True
    success_url = reverse_lazy('area_do_candidato')  # Redireciona para a área do candidato após login
#**********************************************************************************************************

@require_POST  # Garante que o logout só será feito via método POST
def logout_view(request):
    logout(request)  # Encerra a sessão do usuário
    request.session.flush()  # Limpa todos os dados da sessão
    return redirect('pagina_inicial')  # Redireciona para a página inicial após o logout
#**********************************************************************************************************

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('area_do_candidato')  # Redireciona usuários autenticados

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('area_do_candidato')  # Redireciona após login bem-sucedido
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})
#**********************************************************************************************************

# View para exibir a página de confirmação do logout
def logout_confirm(request):
    return render(request, 'logout_confirm.html')
#**********************************************************************************************************

def update_info_pessoal(request):
    if request.method == 'POST':
        user = request.user
        user.nome_completo = request.POST.get('nome_completo')
        user.cpf = request.POST.get('cpf')
        user.save()
        messages.success(request, 'Informações pessoais atualizadas com sucesso.')
        return redirect('area_do_candidato')
#**********************************************************************************************************

def update_inscricao(request):
    if request.method == 'POST':
        inscricao = Inscricao.objects.get(candidato=request.user)
        inscricao.data_inscricao = request.POST.get('data_inscricao')
        inscricao.status = request.POST.get('status_inscricao')
        inscricao.save()
        messages.success(request, 'Informações da inscrição atualizadas com sucesso.')
        return redirect('area_do_candidato')
#**********************************************************************************************************

def update_resultados(request):
    if request.method == 'POST':
        inscricao_id = request.POST.get('inscricao_id')
        try:
            # Fetch the inscricao
            inscricao = Inscricao.objects.get(id=inscricao_id)
            
            # Fetch and validate the 'nota'
            nota = request.POST.get('nota')
            if nota:
                inscricao.nota = Decimal(nota)  # Ensure it's converted to Decimal
            else:
                inscricao.nota = None

            # Update the approval status
            status_aprovacao = request.POST.get('status_aprovacao')
            inscricao.aprovado = (status_aprovacao == 'Aprovado')
            
            # Save the updated data
            inscricao.save()

            messages.success(request, 'Resultados atualizados com sucesso!')
            return redirect('area_do_candidato')

        except (Inscricao.DoesNotExist, ValidationError, Decimal.InvalidOperation):
            messages.error(request, 'Ocorreu um erro ao atualizar os resultados. Verifique os dados.')
            return redirect('area_do_candidato')

    return render(request, 'area_do_candidato.html')
#**********************************************************************************************************

def update_info_pessoal(request):
    if request.method == 'POST':
        # Assume form processing here
        try:
            # Update user's info successfully
            messages.success(request, 'Informações atualizadas com sucesso!')
            return redirect('area_do_candidato')
        except:
            messages.error(request, 'Ocorreu um erro ao atualizar as informações.')
            return redirect('area_do_candidato')
#**********************************************************************************************************       

def my_view(request):
    # Example of success message
    messages.success(request, 'Your data was saved successfully.')
    
    # Example of error message
    messages.error(request, 'There was an error processing your request.')

    return redirect('some_view')
#**********************************************************************************************************

def update_inscricao(request):
    if request.method == 'POST':
        # Assuming 'data_inscricao' is the name of the field in your form
        data_inscricao_str = request.POST.get('data_inscricao')
        
        # Try to convert the date into the correct format
        try:
            data_inscricao = datetime.strptime(data_inscricao_str, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            # If the date format is incorrect, return an error
            raise ValidationError('Data de inscrição inválida. O formato correto é YYYY-MM-DD HH:MM:SS.')

        # Continue processing your form and updating the 'inscricao' object
        inscricao = Inscricao.objects.get(id=request.POST.get('inscricao_id'))
        inscricao.data_inscricao = data_inscricao
        inscricao.status = request.POST.get('status_inscricao')
        inscricao.save()

        # Redirect or render a success message
        return redirect('area_do_candidato')
    
    return render(request, 'update_inscricao.html')
#**********************************************************************************************************

def generate_qr_code(inscricao):
    # URL ou dado que você quer codificar no QR Code (pode ser a URL para os detalhes da inscrição)
    data = f"http://127.0.0.1:8000/inscricao/{inscricao.id}/detalhes"
    
    # Crie o QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Crie uma imagem do QR Code em memória
    img = qr.make_image(fill='black', back_color='white')
    buffered = BytesIO()
    img.save(buffered, format="PNG")

    # Converta a imagem para base64 para ser embutida no HTML
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

    # Retorne a URL de dados para ser usada no template HTML
    return f"data:image/png;base64,{img_str}"
#**********************************************************************************************************

def view_inscricao(request, inscricao_id):
    inscricao = get_object_or_404(Inscricao, id=inscricao_id)
    context = {
        'inscricao': inscricao
    }
    return render(request, 'template_name.html', context)
#**********************************************************************************************************

def user_profile(request, user_id):
    usuario = get_object_or_404(Usuario, id=user_id)
    return render(request, 'area_do_candidato.html', {'usuario': usuario})
#**********************************************************************************************************
def search_schools_by_address(request):
    address = request.GET.get('address', '')
    schools = School.objects.filter(address__icontains=address)
    return JsonResponse({'schools': list(schools.values('name', 'neighborhood', 'address'))})
#**********************************************************************************************************

def search_schools_by_cep(request):
    address = request.GET.get('address', '')
    neighborhood = request.GET.get('neighborhood', '')
    cep = request.GET.get('cep', '')

    # Filtering by address, neighborhood, and cep
    schools = School.objects.all()

    if address:
        schools = schools.filter(address__icontains=address)
    if neighborhood:
        schools = schools.filter(neighborhood__icontains=neighborhood)
    if cep:
        schools = schools.filter(cep__icontains=cep)

    return JsonResponse({'schools': list(schools.values('name', 'neighborhood', 'address', 'cep'))})
#**********************************************************************************************************
# Function-based view to search for Bairro based on logradouro or CEP
def search_bairro(request):
    query = request.GET.get('query', '')  # Get the search input from the request
    if query:
        # Search for matching entries in the Bairro model
        bairros = Bairro.objects.filter(
            logradouro_nome__icontains=query
        ) | Bairro.objects.filter(cep__icontains=query)

        # Convert results to a list of dictionaries
        results = list(bairros.values('logradouro_nome', 'bairro_distrito', 'cep'))

        # Return the search results as a JSON response
        return JsonResponse({'results': results})
    
    # If no query, return an empty result set
    return JsonResponse({'results': []})
#**********************************************************************************************************

def list_bairros(request):
    bairros = Bairro.objects.all()  # Fetch all Bairro entries
    return render(request, 'bairros/list.html', {'bairros': bairros})
#**********************************************************************************************************
def get_bairros(request):
    bairros = list(Bairro.objects.values('id', 'logradouro_nome', 'bairro_distrito', 'cep'))
    return JsonResponse({'bairros': bairros})
#**********************************************************************************************************
class CustomLoginView(LoginView):
    form_class = CPFLoginForm
    template_name = 'login.html'
    
    def form_valid(self, form):
        cpf = form.cleaned_data.get('username')  # CPF field is treated as the username
        password = form.cleaned_data.get('password')
        
        user = authenticate(self.request, cpf=cpf, password=password)
        if user is not None:
            login(self.request, user)
            return redirect('area_do_candidato')
        else:
            form.add_error(None, "CPF ou senha inválidos.")
            return self.form_invalid(form)
#**********************************************************************************************************
class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = 'registration/password_reset.html'  # Template for the password reset form
    email_template_name = 'registration/password_reset_email.html'  # Template for the reset email
    success_url = reverse_lazy('login')  # Redirect to login after the email is sent
#**********************************************************************************************************

def test_email(request):
    send_mail(
        'Test Email',
        'This is a test email from Django.',
        'your-email@gmail.com',
        ['recipient-email@example.com'],
        fail_silently=False,
    )
    return HttpResponse('Email sent!')
#**********************************************************************************************************

# Only allow staff users to access
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard_view(request):
    inscricoes = Inscricao.objects.all()  # Fetch all registrations or any other data
    context = {'inscricoes': inscricoes}
    return render(request, 'admin/admin_dashboard.html', context)


@user_passes_test(lambda u: u.is_staff)
def export_inscricoes_to_csv(request):
    inscricoes = Inscricao.objects.all()

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="inscricoes.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'CPF', 'Email'])

    for inscricao in inscricoes:
        writer.writerow([inscricao.id, inscricao.candidato.nome_completo, inscricao.candidato.cpf, inscricao.candidato.email])

    return response
#**********************************************************************************************************

class CustomAdminLoginView(LoginView):
    template_name = 'registration/admin_login.html'
