from django.db import models

class Notebook(models.Model):
	name = models.CharField(max_length=200)
	owner = models.IntegerField()
	def __unicode__(self):
		return self.name
	
class Note(models.Model):
	owner = models.IntegerField()
	subject = models.CharField(max_length=200)
	content = models.TextField(blank='True', null='True')
	notebook = models.ForeignKey(Notebook, blank='True', null='True')
	create_date = models.DateTimeField('date created', auto_now_add=True)
	mod_date = models.DateTimeField('date modified',auto_now=True)
	tags = models.TextField(max_length=200, blank='True', null='True')
	def __unicode__(self):
		return self.subject
	
class Tag(models.Model):
	name = models.CharField(max_length=50)
