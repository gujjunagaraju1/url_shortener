from django.db import models
import string
import random


class UrlData(models.Model):
    original=models.CharField(max_length=400)
    short=models.CharField(max_length=20,unique=True)
    def __str__(self) :
        return f'{self.original} converted to {self.short}'
    @classmethod
    def create(self,original):
        short="".join(random.choice(string.ascii_letters)for x in range(10))
        try:
            obj=self.objects.create(original=original,short=short)
        except:
            obj=self.objects.get(original=original)
        return obj
            

# Create your models here.
