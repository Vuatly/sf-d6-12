from django import forms  
from p_library.models import Author, Book
  


class BookForm(forms.ModelForm):  
    class Meta:  
        model = Book  
        fields = '__all__'


