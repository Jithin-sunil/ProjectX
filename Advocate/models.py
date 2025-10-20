from django.db import models
from Guest.models import *
from PoliceStation.models import *
# Create your models here.

class tbl_request(models.Model):
    request_casedesc=models.CharField(max_length=50)
    request_date=models.DateField(auto_now_add=True)
    advocate=models.ForeignKey(tbl_advocate,on_delete=models.CASCADE)
    case=models.ForeignKey(tbl_case,on_delete=models.CASCADE)
    advocate=models.ForeignKey(tbl_advocate,on_delete=models.CASCADE)
    request_status=models.IntegerField(default=0)
    request_bailfile=models.FileField(upload_to="Assets/BailFiles/",null=True,blank=True)