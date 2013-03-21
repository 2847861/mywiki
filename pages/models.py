from django.db import models

# Create your models here.


class Page(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
         return self.name
		
class Choice(models.Model):
    page = models.ForeignKey(Page)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)	
    def __unicode__(self):
        return self.choice_text

