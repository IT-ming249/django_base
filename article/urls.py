from . import views
from django.urls import path


urlpatterns = [
    path("test", views.article_test, name="article_test"),
    path("one2many",views.one_to_many, name="one2many"),
]