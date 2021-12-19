"""
Django settings for babys project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os.path
import time
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*x-w$nhwot)g=w8iq(vghae@1wg-lovlq$o_icw$=h=@bhlcw4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'index',
    'commodity',
    'shopper',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'babys.urls'

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

WSGI_APPLICATION = 'babys.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'babys',
        'USER': "root",
        'PASSWORD': "123456",
        'HOST': "192.168.1.9",
        'PORT': "3306",
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'pstatic'),
)

# 官方文档中给出了详细的介绍。处理由MEDIA_ROOT提供的媒体文件的URL，用于管理存储的文件。如果设置为非空值，它必须以斜杠结尾。
MEDIA_URL = '/media/'
# MEDIA_ROOT是保存用户上传文件的目录的绝对文件系统路径。因为是绝对路径，所以使用os.path.join方法生产出MEDIA_ROOT
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
if not os.path.exists("./logDir/toolLog/"):
    os.makedirs("./logDir/toolLog/")
if not os.path.exists("./logDir/toolLog/{}/".format(today)):
    os.makedirs("./logDir/toolLog/{}/".format(today))
BASE_LOG_DIR = os.path.join(BASE_DIR, "./logDir/toolLog/{}/".format(today))
infologName = today + "_info.log"
collectlogName = today + "_collect.log"
errlogName = today + "_err.log"
LOGGING = {
    'version': 1,  # 保留字
    'disable_existing_loggers': False,  # 禁用已经存在的logger实例
    'formatters': {  # 日志文件的格式
        'standard': {  # 详细的日志格式
            'format': '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d][%('
                      'levelname)s][%(message)s] '
        },
        'simple': {  # 简单的日志格式
            'format': '[%(asctime)s][%(levelname)s][%(filename)s:%(lineno)d]=%(message)s'
            #     '%(asctime)s %(filename)s %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s'
        },
        'collect': {  # 定义一个特殊的日志格式
            'format': '[#]%(message)s'
        }
    },
    'filters': {  # 过滤器
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {  # 处理器
        'console': {  # 在终端打印
            'level': 'DEBUG',
            'filters': ['require_debug_true'],  # 只有在Django debug为True时才在屏幕打印日志
            'class': 'logging.StreamHandler',  #
            'formatter': 'simple'
        },
        'default': {  # 默认的
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, infologName),  # 日志文件
            'maxBytes': 1024 * 1024 * 500,  # 日志大小 500M
            'backupCount': 5,  # 最多备份几个
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'error': {  # 专门用来记错误日志
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, errlogName),  # 日志文件
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'collect': {  # 专门定义一个收集特定信息的日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 日志文件指定为多大(5M)， 超过大小(5M)重新命名，然后写新的日志文件
            'filename': os.path.join(BASE_LOG_DIR, collectlogName),
            'maxBytes': 1024 * 1024 * 500,  # 日志大小 500M
            'backupCount': 5,  # 文件数量
            'formatter': 'collect',
            'encoding': "utf-8"
        }
    },
    'loggers': {
        '': {  # 默认的logger应用如下配置
            'handlers': ['default', 'console', 'error'],  # 上线之后可以把'console'移除
            'level': 'DEBUG',
            'propagate': True,  # 向不向更高级别的logger传递
        },
        'collect': {  # 名为 'collect'的logger还单独处理
            'handlers': ['console', 'collect'],
            'level': 'INFO',
        }
    },
}
