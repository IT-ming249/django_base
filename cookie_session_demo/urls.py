from . import views
from django.urls import path

app_name = "cook_session"
urlpatterns = [
    path('', views.index, name='index'),
    path("add",views.add_cookie, name='add_cookie'),
    path("delete",views.delete_cookie, name='delete_cookie'),
    path("get",views.get_cookie, name='get_cookie'),
    path("session_add",views.add_session,name='session_add'),
    path("session_get",views.get_session,name='session_get'),
]