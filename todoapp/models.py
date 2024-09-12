from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Task(models.Model):
    level=(('Low','Low'),
           ('Medium','Medium'),
           ('Hard','Hard'))
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField()
    priority=models.CharField(max_length=100,choices=level,default='Low')
    completed=models.BooleanField()
    create_date=models.DateField(default=datetime.now)

