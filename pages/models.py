from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    head = models.CharField(max_length=100)
    nav = models.CharField(max_length=100)    
    section = models.CharField(max_length=100)    
    content = models.TextField(max_length=10000)
    image = models.CharField(max_length=200)
    
    def __unicode__(self):
         return self.title

class Navig(models.Model):
	page = models.ForeignKey(Page)
	title = models.CharField(max_length=100)
	nav1 = models.CharField(max_length=100)
	nav2 = models.CharField(max_length=100)
	nav3 = models.CharField(max_length=100)
	
	def __unicode__(self):
	    return self.title
		
class Sect(models.Model):
	page = models.ForeignKey(Page)
	title = models.CharField(max_length=100)
	sect1 = models.CharField(max_length=100)
	sect2 = models.CharField(max_length=100)
	sect3 = models.CharField(max_length=100)
	
	def __unicode__(self):
	   return self.title
	   
class Cont(models.Model):
	page3 = models.ForeignKey(Page)
	titre = models.CharField(max_length=100)
	text1 = models.TextField(max_length=10000)
	text2 = models.TextField(max_length=10000)
	text3 = models.TextField(max_length=10000)
	text4 = models.TextField(max_length=10000)
	
	def __unicode__(self):
	   return self.titre
	   
class Img(models.Model):
	page4 = models.ForeignKey(Page)
	title = models.CharField(max_length=100)
	image1 = models.CharField(max_length=200)
	image2 = models.CharField(max_length=200)
	image3 = models.CharField(max_length=200)
	image4 = models.CharField(max_length=200)
	
	def __unicode__(self):
	   return self.title
	

