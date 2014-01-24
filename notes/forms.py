from django import forms
from models import Note, Notebook

class NoteForm(forms.ModelForm):
	
	class Meta:
		model = Note
		fields = ('subject', 'content', 'notebook', 'tags')
		
class NoteBookForm(forms.ModelForm):
	
	class Meta:
		model = Notebook
		fields = ('name',)
