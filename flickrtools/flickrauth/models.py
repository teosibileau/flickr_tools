from django.db import models

class Access(models.Model):
    user=models.CharField(max_length=50)
    key=models.CharField(max_length=40)
    secret=models.CharField(max_length=20)
    class Meta:
        verbose_name='Access'
        verbose_name_plural='Accesses'
    
