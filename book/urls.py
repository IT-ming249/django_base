from . import views
from django.urls import path

app_name = 'book'
urlpatterns = [
    #http://127.0.0.1:8000/book?id=3&name=mm ↓
    path("", views.book_search_id, name = 'book'),
    #http://127.0.0.1:8000/book/1 ↓
    path("int/<int:page>", views.book_search_detail_int, name = 'book_int'),
    path("str/<name>/<int:page>", views.book_search_detail_str, name = 'book_str'),
    path("slug/<slug:page>", views.book_search_detail_slug, name = 'book_slug'),
    path("path/<path:page>", views.book_search_detail_path, name = 'book_path'),
    path("add",views.add_book, name = 'book_add'),
    path("query",views.query_book, name = 'book_query'),
    path("order",views.order_view, name = 'book_order'),
    path("modify",views.modify_book, name = 'book_modify'),
    path("delete",views.delete_book, name = 'book_delete'),
    path("tag",views.book_tag,name = 'book_tag'),
]