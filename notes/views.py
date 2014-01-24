from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
#from django.template import RequestContext, loader
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
import datetime
from notes.models import Note, Notebook
from notes.forms import NoteForm, NoteBookForm


@login_required
def index(request):
	notes_list = Note.objects.filter(owner = request.user.id)
	notes_count = Note.objects.filter(owner = request.user.id).count()
	notebook_list = Notebook.objects.order_by('-name')
	args = {'notes_list': notes_list,
			   'notebook_list': notebook_list,
			   'user_username': request.user.username,
			   'user_id': request.user.id,
			   'notes_count': notes_count
			   }
	return render(request,'notes/index.html',args)

@login_required
def new_n(request):
	notebook_list = Notebook.objects.order_by('-name')
	notes_count = Note.objects.filter(owner = request.user.id).count()
	if request.POST:
		form = NoteForm(request.POST)
		if form.is_valid():
			newnote = form.save(commit=False)
			newnote.owner = request.user.id
			newnote.save()
		return HttpResponseRedirect('/notes/')
	else:
		form = NoteForm()
		args = {'notebook_list': notebook_list,
				'notes_count': notes_count,
				'user_username': request.user.username,
				'user_id': request.user.id}
			
		args.update(csrf(request))
		args['form'] = form
		return render_to_response('notes/new_n.html', args)

@login_required	
def edit_n(request, Note_id):
	
	if request.POST:
		form = NoteForm(request.POST, instance=Note.objects.get(pk=Note_id))
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/notes/')
	else:
		notebook_list = Notebook.objects.order_by('-name')
		notes_count = Note.objects.filter(owner = request.user.id).count()
		n = Note.objects.get(pk=Note_id)
		form = NoteForm(request.POST)
		args = {'n': n,
				'notebook_list': notebook_list,
				'notes_count': notes_count}
		args.update(csrf(request))
		args['form'] = form
		return render_to_response('notes/edit_n.html', args)
	
@login_required
def open_n(request, Note_id):
	notebook_list = Notebook.objects.order_by('-name')
	notes_count = Note.objects.filter(owner = request.user.id).count()
	n = Note.objects.get(pk=Note_id)
	args = {'n': n,
			   'notes_count': notes_count,
			   'notebook_list': notebook_list}
	return render(request,'notes/open_n.html',args)

@login_required
def new_nb(request):
	notebook_list = Notebook.objects.order_by('-name')
	notes_count = Note.objects.filter(owner = request.user.id).count()
	if request.POST:
		form = NoteBookForm(request.POST)
		if form.is_valid():
			newnotebook = form.save(commit=False)
			newnotebook.owner = request.user.id
			newnotebook.save()
		return HttpResponseRedirect('/notes/')
	else:
		form = NoteBookForm()
		args = {'notebook_list': notebook_list,
				'notes_count': notes_count,
				'user_username': request.user.username,
				'user_id': request.user.id}
			
		args.update(csrf(request))
		args['form'] = form
		return render_to_response('notes/new_nb.html', args)

@login_required
def nb_index(request, NoteBook_id):
	notes_list = Note.objects.filter(owner = request.user.id, notebook = NoteBook_id)
	nb_select = Notebook.objects.get(pk = NoteBook_id)
	notes_count = Note.objects.filter(owner = request.user.id).count()
	notebook_list = Notebook.objects.order_by('-name')
	args = {'notes_list': notes_list,
			'nb_select': nb_select,
			'notebook_list': notebook_list,
			   'user_username': request.user.username,
			   'user_id': request.user.id,
			   'notes_count': notes_count
			   }
	return render(request,'notes/nb_index.html',args)


