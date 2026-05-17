import os
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from the .env file
load_dotenv(os.path.join(BASE_DIR, '.env'))

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings loaded dynamically from environment variables
SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-insecure-key-for-dev-only')

# Converts the environment string 'True' or 'False' into a real Python Boolean
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Reads hosts from .env split by commas, adapting smoothly between local and Railway URLs
ALLOWED_HOSTS = [host.strip() for host in os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',') if host]

# Explicitly allow Railway's private domain structure if deployed
if os.getenv('RAILWAY_STATIC_URL'):
    ALLOWED_HOSTS.append('.railway.app')
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # THE PRODUCTION STATIC ENGINE
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pasel_project.urls'
WSGI_APPLICATION = 'pasel_project.wsgi.application'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # This tells Django to look for a 'templates' folder in your main directory
        'DIRS': [BASE_DIR / 'templates'], 
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
# Database, Static, and Media Config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# The production repository where WhiteNoise compiles assets for launch
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# WhiteNoise storage optimization for caching and compressing assets
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media Files (Slideshow and Gallery Uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Authentication Redirects (Preserved Core Routing)
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'