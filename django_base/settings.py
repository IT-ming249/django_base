"""
Django settings for django_base project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-mu4)wmul(fk6d1o!(#q9s+*+lvib6x&%5u+2w-^jq3&+&#s4ua"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "book", #安装app,以识别models
    "movie",  #安装app
    "article",
    "sale",
    "form_demo"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware", #验证csrf_token
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_base.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates", #模板引擎
        "DIRS": [os.path.join(BASE_DIR,"templates")],                 #配置模板文件夹，模板文件在这个文件夹下存储
        "APP_DIRS": True,                                             #Ture 在安装app后可读取app下的templates内的模板文件
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            #加入下面这行，html中可以省略{% load static%}
            'builtins':["django.templatetags.static"]
        },
    },
]

WSGI_APPLICATION = "django_base.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

#修改数据库设置
DATABASES = {
    "default": {
        #引擎，eg:mysql/sqlite3/postgresql
        "ENGINE": "django.db.backends.mysql",
        #数据库名
        "NAME": "database_demo",
        #连接数据库的用户名
        "USER": "root",
        #密码
        "PASSWORD": "SQL123",
        #主机地址
        "HOST": "127.0.0.1",
        #端口号
        "PORT": "3306",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Shanghai"  #时区

USE_I18N = True

USE_TZ = False  #是否使用时区


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

#设置静态文件存放路径↓
STATICFILES_DIRS =[
  BASE_DIR/'static'
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
#数据库的默认主键类型↓
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SESSION_ENGINE = "django.contrib.sessions.backends.db" #session存储在数据库中
