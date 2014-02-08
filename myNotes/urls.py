from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from myNotes.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myNotes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	# Login / logout.
	(r'^$', main_page),

    # Login / logout.
    #(r'^login/$', 'django.contrib.auth.views.login'),
    #(r'^logout/$', logout_page),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^notes/', include('notes.urls', namespace="notes")),
	#url('^markdown/', include( 'django_markdown.urls')),
)
