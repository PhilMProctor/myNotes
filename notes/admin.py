from django.contrib import admin

from notes.models import Note, Notebook

admin.site.register(Note)
admin.site.register(Notebook)
