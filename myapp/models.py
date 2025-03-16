from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


CATEGORY_CHOICES=[
    ('professional','professional'),
    ('Non Professional','Non Professional')
]

class Task(models.Model):
    srno=models.AutoField(auto_created=True,primary_key=True)
    title= models.CharField(max_length=25)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False,blank=True,)
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=20,default='professional')
    description=models.TextField(blank=True,null=True)

    def __str__(self) -> str:
        return self.title
    
    
    
    
    
    
    
    