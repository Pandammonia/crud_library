from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		exclude = ('slug',)

class AuthorForm(forms.ModelForm):
	class Meta:
		model = Author
		exclude = ('slug',)