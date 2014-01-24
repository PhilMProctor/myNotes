from django.conf.urls import patterns, url

from notes import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^(?P<Note_id>\d+)/edit_n/$', views.edit_n, name='edit_n'),
	url(r'^(?P<Note_id>\d+)/open_n/$', views.open_n, name='open_n'),
	url(r'^(?P<NoteBook_id>\d+)/nb_index/$', views.nb_index, name='nb_index'),
	url(r'^new_n/$', views.new_n, name='new_n'),
	url(r'^new_nb/$', views.new_nb, name='new_nb'),
)
