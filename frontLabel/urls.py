from . import views
from django.urls import path

app_name = 'frontLabel'

urlpatterns = [
    path('if', views.if_label, name='if_label'),
    path('for',views.for_in_label,name='for_in_label'),
]