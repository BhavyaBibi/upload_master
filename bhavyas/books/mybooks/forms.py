from django import forms
from mybooks.models import books
class booksform(forms.ModelForm):
    class Meta():
        model=books
        fields='__all__'
