from . import views
from django.urls import path

app_name = 'sale'

urlpatterns = [
    path('', views.sale_index, name='sale_index'),
    path("avg", views.avg_view, name='sale_avg'),
    path("count",views.count_view, name='sale_count'),
    path("max_min", views.max_min_view, name='sale_max_min'),
    path("sum",views.sum_view, name='sale_sum'),
    path("f",views.f_view, name='sale_f'),
    path("q",views.q_view, name='sale_q'),
]