from . import views
from django.urls import path

app_name = 'frontLabel'

urlpatterns = [
    path('if', views.if_label, name='if_label'),
    path('for',views.for_in_label,name='for_in_label'),
    path("with",views.with_label,name='with_label'),
    path("url",views.url_label,name='url_label'),
    path("filter",views.filter,name='filter'),
    path("pindex",views.include_html_model,name='pindex'),
    path("sta",views.static_example,name='static'),
]