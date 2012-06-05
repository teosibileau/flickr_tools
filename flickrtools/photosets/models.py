from django.db import models
from datetime import datetime
from tagging.fields import TagField
from flickrauth.models import Access

class Photoset(models.Model):
    access=models.ForeignKey(Access,related_name='photosets')
    uid = models.BigIntegerField(unique=True,null=True,blank=True)
    title = models.CharField(max_length=200)
    last_checked=models.DateTimeField(editable=False,null=True,blank=True)
    tags=TagField()
    class Meta:
        verbose_name='PhotoSet'
        verbose_name_plural='Photosets'
    
    def save(self):
        super(Photoset,self).save()
    
    def __unicode__(self):
        return u"%s"%self.title
    
