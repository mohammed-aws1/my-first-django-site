from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.text import slugify

# Create your models here.
class Posts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    content = models.TextField(max_length=5000,blank=True,null=True)
    slug = models.SlugField(null=True,blank=True)
    time_created = models.DateTimeField(default=datetime.datetime.now())
    img = models.ImageField(upload_to='',default='aws.jpg',blank=True,null=True)
    tags = models.CharField(max_length=10,blank=True,null=True)
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Posts,self).save(*args,**kwargs)
    def __str__(self):
        return self.title