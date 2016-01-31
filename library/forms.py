from django import forms

from .models import Books

class BooksForm(forms.Form):
    doc_file = forms.FileField(
            label='Select a file',
            help_text='max. 42 megabytes'
            )
    #class Meta:
    #    model = Books
    #    fields = ['title']
    #file_path = forms.FileField(label='Select a book')
