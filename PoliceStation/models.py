from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.
class tbl_case(models.Model):
    case_number=models.CharField(max_length=50)
    case_section=models.CharField(max_length=100)
    case_content=models.CharField(max_length=300)
    case_file=models.FileField(upload_to="Assets/Files/Case")
    case_datetime=models.DateTimeField(auto_now_add=True)
    type=models.ForeignKey(tbl_type,on_delete=models.CASCADE)
    policestation=models.ForeignKey(tbl_policestation,on_delete=models.CASCADE)