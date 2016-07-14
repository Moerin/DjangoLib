from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.shortcuts import redirect

from .forms import BooksForm
from .models import Books


class BooksCreate(FormView):
    template_name = 'book_form.html'
    form_class = BooksForm

    def get(self, request, *args, **kwargs):
        import ipdb; ipdb.set_trace()  # XXX BREAKPOINT

        if request.GET['msg'] == 'good':
            pass

        # There is errors
        else:
            pass

    def post(self, request, *args, **kwargs):

        form = BooksForm(request.POST, request.FILES)
        # Form is not valid
        if form.is_valid():
            newbook = Books(title=request.POST['title'],
                            author=request.POST['author'],
                            file_path=request.FILES['file_path'])
            newbook.save()
            bar = 'good'
        else:
            bar = form.errors

        return redirect('index/?msg=%s' % bar)

    def form_valid(self, form):
        return super(BooksCreate, self).form_valid(form)
