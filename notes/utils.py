# Utilities script to contain the following:
# Tag Cloud
import re
from notes.models import Note
from django.db.models import Count

# Tag Cloud

def tag_cloud():
	rtt = Note.objects.values_list('tags', flat=True) #raw tag tuple
	rtl = ",".join(rtt)
	#raw_tag_list = Note.objects.get().tags
	tag_list = rtl.split(',')
	
	return tag_list
