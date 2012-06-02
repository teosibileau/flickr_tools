from django.db import models

class Photoset(models.Model):
    uid = models.BigIntegerField(unique=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1700)
    added = models.BooleanField(0)
    class Meta:
        verbose_name='PhotoSet'
        verbose_name_plural='Photosets'
    
    def __unicode__(self):
        return u"%s"%self.title

class Photo(models.Model):
    photoset = models.ForeignKey(Photoset,related_name='photos')
    uid = models.BigIntegerField(unique=True)
    title = models.CharField(max_length=600)
    url = models.CharField(max_length=500)
    added = models.BooleanField(0)
    class Meta:
        verbose_name='Photo'
        verbose_name_plural='Photos'
    
    def __unicode__(self):
        return u"%s: %s"%(self.photoset.title,self.title)