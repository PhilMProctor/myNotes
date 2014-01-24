from django.http import HttpResponse
from django.http import HttpResponseRedirect
#from django.template import RequestContext, loader
from django.shortcuts import render
from django.core.context_processors import csrf
import datetime

from notes.models import Note, Notebook
from forms import NoteForm

def index(request):
	notes_list = Note.objects.order_by('-mod_date')
	notebook_list = Notebook.objects.order_by('-name')
	context = {'notes_list': notes_list,
			   'notebook_list': notebook_list}
	return render(request,'notes/index.html',context)

def detail(request, Note_id):
    return HttpResponse("You're looking at note %s." % Note_id)

def edit(request):
	if request.POST:
		form = NoteForm(request.POST)
		if form.is_valid():
			form.save()
			
			return HttpResponseRedirect('/notes/index')
		else:
			form = NoteForm()
			
		args = {}
		args.update(csrf(request))
		
		args['form'] = form
		
		return render_to_response('edit_note.html', args)

"""def edit(request, Note_id):
	n = Note.objects.get(pk=Note_id)
	notebook_list = Notebook.objects.order_by('-name')
	context = {'notebook_list': notebook_list,
			   'n': n}
	return render(request,'notes/edit.html',context)

def update(request, Note_id, nNotebook, nSubject, nContent, nTags=None):
	Subject=str(nSubject)
	Content=str(nContent)
	Tags=str(nTags)
	#n = Note.objects.get(pk=Note_id)
	#nCdate=str(nCdate)
	#Cdate= datetime.datetime.strftime(nCdate, '%b %d %Y %I:%M%p')
	#create2=create.replace('.', ' ')
	#now = str(datetime.datetime.now())
	#nMdate = datetime.datetime.strptime(now, '%b %d %Y %I:%M%p')
	#create3 = datetime.datetime.strptime(create2, '%b %d %Y %I:%M%p')
	uNote = Note(id=Note_id, notebook=nNotebook, subject=Subject, content=Content, tags=Tags)
	uNote.save()
	notes_list = Note.objects.order_by('-mod_date')
	notebook_list = Notebook.objects.order_by('-name')
	context = {'notes_list': notes_list,
			   'notebook_list': notebook_list}
	return render(request,'notes/index.html',context)
"""
def open(request, Note_id):
	n = Note.objects.get(pk=Note_id)
	context = {'n': n}
	return render(request,'notes/open.html',context)

def new(request):
	return HttpResponse("You're now creating a new note")
