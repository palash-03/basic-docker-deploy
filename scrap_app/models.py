from django.db import models
# from django.contrib.gis.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
	employee = models.ForeignKey(User,on_delete=models.CASCADE)
	projects_name = models.CharField(max_length=10)
	project_hours = models.CharField(max_length=10)
	project_time = models.CharField(max_length=10)
	project_date = models.DateField()
	developer_name = models.CharField(max_length=255)