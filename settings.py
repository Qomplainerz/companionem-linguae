import os
from pathlib import Path
from dotenv import load_dotenv # Import für die .env-Datei

# 1. Lade die Umgebungsvariablen aus der .env-Datei

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================================================
# WICHTIGE SICHERHEITSEINSTELLUNGEN
# ==============================================================

SECRET_KEY = os.getenv('SECRET_KEY', 'dgango-insecure-fallback-key-bitte-in-env-setzen')

# ==============================================================
# DEBUG MODUS
# ==============================================================

DEBUG = os.getenv('DEBUG') == 'False'

# ==============================================================
# ALLOWED HOSTS
# ==============================================================

allowed_hosts_env = os.getenv('ALLOWED_HOSTS')
if allowed_hosts_env:
    ALLOWED_HOSTS = allowed.hosts_env.split(',')
else:
    ALLOWED_HOSTS = []

# =============================================================
# APPS & MIDDLEWARE (Django Standard)
# =============================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mein_projekt.urls' # Ersetze 'mein_projekt' durch deinen Ordnernamen, falls anders!

TEMPLATES = [
    {
	'BACKEND': 'django.template.backends.django.DjangoTemplates',
	'DIRS': [],
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

WSGI_APPLICATION = 'mein_projekt.wsgi.application' # Ersetze 'mein_projekt' auch hier"! 

# ===============================================
# DATENBANK (Deine MySQL Konfiguration)
# ===============================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
	'NAME': os.getenv('DB_NAME'),
	'USER': os.getenv('DB_USER'),
	'PASSWORD': os.getenv('DB_PASSWORD'),
	'HOST': os.getenv('DB_HOST'),
	'PORT': os.getenv('DB_PORT'),
	'OPTIONS': {
	    # Wichtig für MySQL/MariaDB Kompatibilität
	    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
	},
    }
}

# ================================================
# PASSWORT VALIDIERUNG
# ================================================

AUTH_PASSWORD_VALIDATORS = [
    {
	'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
	'NAME': 'django.contrib.auth.pssword_validation.MinimumLengthValidator',
    },
    {
	'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
	'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ======================================================
# INTERNATIONALISIERUNG (Sprache & Zeit)
# ======================================================

LANGUAGE_CODE = 'en-en' # Auf Englisch gestellt
TIME_ZONE = 'Europe/Berlin' # Auf deutsche Zeit gestellt
USE_I18N = True
USE_TZ = True

# ======================================================
# STATIC FILES (CSS, JavaScript, Images)
# ======================================================

STATIC_URL = 'static/'

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
