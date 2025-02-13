from . import views
from django.urls import path

# 指定app名称(应用命名空间)
app_name = 'movie'

urlpatterns = [
    path("list", views.movie_list,name='movie_list'),
    path("detail/<int:movie_id>", views.movie_detail, name = 'movie_detail'),
    path("",views.movie_index, name='movie_index'),
    path("info/<int:movie_id>",views.movie_info,name='movie_info')
]

