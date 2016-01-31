from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Books
from .forms import BooksForm

class BooksCreate(CreateView):
    #model = Books
    #fields = ['title']
    template_name = 'book_form.html'
    form_class = BooksForm

# TODO OTHER VIEW
