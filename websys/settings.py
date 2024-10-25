from pathlib import Path
import os
#import environ



# No arquivo settings.py

SECURE_SSL_REDIRECT = False  # Desativa redirecionamento automático para HTTPS
SESSION_COOKIE_SECURE = False  # Garante que cookies de sessão não exijam HTTPS
CSRF_COOKIE_SECURE = False  # Garante que o CSRF não exija HTTPS


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lzc)l!c$ew3kylcssvcvdr^5^ww9=wp$ivt@&$o6pei+!0$oug'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['54.233.92.107', '15.228.59.223', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'websys.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'websys.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',  # Use 'mysql' para o backend
#         'NAME': 'eja2024',
#         'USER': 'root',
#         'PASSWORD': '@Drik16091985',
#         'HOST': 'localhost',   # Ou o IP do servidor MySQL
#         'PORT': '3306',        # Porta padrão do MySQL
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'

# Diretório onde seus arquivos estáticos estão localizados
STATICFILES_DIRS = [ 
    BASE_DIR / 'static',  # Ou 'static/' dependendo de como está o BASE_DIR
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')




# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'login'  # URL para onde redireciona se o usuário não estiver autenticado
LOGIN_REDIRECT_URL = '/listar_funcionarios/'  # URL correspondente à página de listagem de funcionários
LOGOUT_REDIRECT_URL = 'pagina_inicial'  # Para onde redireciona após o logout

# Em settings.py
AUTH_USER_MODEL = 'website.Usuario'  # Substitua 'app_name' pelo nome do app onde o modelo `Usuario` está definido

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default backend
    # Add custom backends if necessary
]



# EMAIL_BACKEND = 'django_ses.SESBackend'
# AWS_ACCESS_KEY_ID = 'your_aws_access_key'
# AWS_SECRET_ACCESS_KEY = 'your_aws_secret_key'
# AWS_SES_REGION_NAME = 'us-east-1'  # or your preferred region
# AWS_SES_REGION_ENDPOINT = 'email.us-east-1.amazonaws.com'

EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_USE_TLS = True
EMAIL_HOST_USER='shelton.oliveira.barbosa@gmail.com'
EMAIL_HOST_PASSWORD='@Drik16091985'


SITE_ATUALIZACAO = False


