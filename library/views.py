from django.views.generic.edit import FormView
from .forms import BooksForm
from .models import Books


class BooksCreate(FormView):
    template_name = 'book_form.html'
    form_class = BooksForm

    def post(self, request, *args, **kwargs):
        form = BooksForm(request.POST, request.FILES)
        # Form is not valid
        if form.is_valid():
            newbook = Books(file_path=request.FILES['file_path'])
            newbook.save()
        else:
            form = BooksForm()

    def form_valid(self, form):
        return super(BooksCreate, self).form_valid(form)
