from . import views
from django.urls import path

app_name = 'csrf'

urlpatterns = [
    path('', views.index, name='index'),
    path("log_in",views.login,name="login"),
]