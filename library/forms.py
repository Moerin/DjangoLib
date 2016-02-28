from django import forms


class BooksForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    file_path = forms.FileField(label='Select a book')
