from . import views
from django.urls import path

app_name = 'form'

urlpatterns = [
    path('', views.index, name='index'),
    path("register", views.register, name="register"),
    path("article", views.article_view, name="article"),
]