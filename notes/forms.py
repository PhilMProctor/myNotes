from django import forms
from models import Note, Notebook
from django_markdown.widgets import MarkdownWidget

class NoteForm(forms.ModelForm):
	
	class Meta:
		model = Note
		fields = ('subject', 'content', 'notebook', 'tags')
		content = forms.CharField( widget=MarkdownWidget() )
		
class NoteBookForm(forms.ModelForm):
	
	class Meta:
		model = Notebook
		fields = ('name',)
