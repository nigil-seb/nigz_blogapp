from django.db import models
import datetime
# Create your models here.
class Blogs(models.Model):
    def __str__(self):
        return self.heading
    heading=models.CharField(max_length=100)
    desc=models.CharField(max_length=200)
    content=models.TextField(default=True)
    date=models.DateField(default=datetime.date.today)