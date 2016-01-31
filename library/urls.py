
from django.conf.urls import url

from .views import BooksCreate

urlpatterns = [
        url(r'^$', BooksCreate.as_view(), name='books_create'),
]
