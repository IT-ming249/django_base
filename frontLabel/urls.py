from . import view
from django.urls import path

app_name = 'frontLabel'

urlpatterns = [
    path('if', view.if_label, name='if_label'),
    path('for',view.for_in_label,name='for_in_label'),
]