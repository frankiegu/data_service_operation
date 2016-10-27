#coding=utf8

"""
Django settings for DataOperation project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2gj68-8%4_hw71$-@v%%2u(p3hwg=j$n9fo$3bar-^%(854o=4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False #生产模式下必须设置域名控制

ALLOWED_HOSTS = ['*']

#设置代理服务基础地址(https?://域名或者IP:端口/)
PROXY_SERVICE_URL = "http://127.0.0.1:80/service/"

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'corsheaders',
    'xadmin',
    'crispy_forms',
    'reversion', #需要pip install django-reversion
    'DataOperation',
    'rest_framework',
    'django_filters',
    'svauth',
    'service',
    'statistics',
    'others',
    'util',
    'util.templatetags',
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (  
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',  
    ),
#   'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_FILTER_BACKENDS': ('rest_framework_filters.backends.DjangoFilterBackend',),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticatedOrReadOnly',),
#   'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'DEFAULT_PAGINATION_CLASS': 'util.rest_settings.RestPagination',
    'PAGE_SIZE': 10,
    'UNICODE_JSON': False,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework_jsonp.renderers.JSONPRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.AdminRenderer',
    ),
}

CORS_ORIGIN_ALLOW_ALL = True
#CORS_ORIGIN_WHITELIST = ('google.com','hostname.example.com')
#CORS_ORIGIN_REGEX_WHITELIST = ('^(https?://)?(\w+\.)?google\.com$', )
CORS_URLS_REGEX = r'^/rest/service/.*$'

MIDDLEWARE_CLASSES = (
#   'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
#   'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'DataOperation.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates').replace('\\','/'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                'django.template.context_processors.request',
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
#                'myapp.myclass.mydef',
            ],
        },
    },
]

WSGI_APPLICATION = 'DataOperation.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'operation_db',
        'USER' : 'db-user',
        'PASSWORD' : 'db-password',
        'HOST' : '127.0.0.1',
        'PORT' : 3306,
        'ATOMIC_REQUESTS': True,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/operation/static/'
STATIC_ROOT = '/website/DataOperation/src/DataOperation/static'
STATIC_PATH= os.path.join(os.path.dirname(__file__), '../static_resource').replace('\\','/')

MEDIA_URL= '/static_resource/'
MEDIA_ROOT = STATIC_PATH

doc_path=os.path.join(os.path.dirname(__file__),'media','uploads','docs').replace('\\','/')
video_path=os.path.join(os.path.dirname(__file__),'media','uploads','videos').replace('\\','/')
image_path=os.path.join(os.path.dirname(__file__),'media','uploads','images').replace('\\','/')

#memcache缓存设置：
CACHES = {
    'default': {
        'BACKEND':'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': [
            'localhost:11211',
        ],
        'TIMEOUT': None, #None表示永远不会过期
    }
}


#邮件配置
EMAIL_HOST = 'smtp.126.com'                   #SMTP地址
EMAIL_PORT = 25                               #SMTP端口
EMAIL_HOST_USER = 'zhiaixuexi@126.com'        #我自己的邮箱
EMAIL_HOST_PASSWORD = 'lx870830'              #我的邮箱密码
EMAIL_SUBJECT_PREFIX = u'[DC-数据服务运营平台]'     #为邮件Subject-line前缀,默认是'[django]'
EMAIL_USE_TLS = True								#与SMTP服务器通信时，是否启动TLS链接(安全链接)。默认是false
#管理员站点
SERVER_EMAIL = 'zhiaixuexi@126.com'            #The email address that error messages come from, such as those sent to ADMINS and MANAGERS.

TIME_ZONE = 'Asia/Shanghai'
#USE_TZ = True

#session设置
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE=60*30 #30分钟session有效期，UTC时间，比实际时间早8小时

