from . import views
from django.urls import path


urlpatterns = [
    path("test", views.article_test, name="article_test"),
    path("one2many",views.one_to_many, name="one2many"),
    path("query1", views.query1, name="query1"),
    path("query2", views.query2, name="query2"),
    path("query3", views.query3, name="query3"),
    path("query4", views.query4, name="query4"),
    path("query5", views.query5, name="query5"),
]