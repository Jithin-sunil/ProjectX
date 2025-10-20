from django.db import models
from Admin.models import* 

# Create your models here.
#admin table
class tbl_user(models.Model):
    user_name=models.CharField(max_length=40)
    user_email=models.CharField(max_length=40)
    user_contact=models.CharField(max_length=40)
    user_address=models.CharField(max_length=40)
    user_gender=models.CharField(max_length=40)
    user_photo=models.FileField(upload_to="Assets/User/Photo/")
    user_password=models.CharField(max_length=40)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)

   
#police station table
class tbl_policestation(models.Model):
    policestation_name=models.CharField(max_length=40)
    policestation_email=models.CharField(max_length=40)
    policestation_contact=models.CharField(max_length=40)
    policestation_address=models.CharField(max_length=40)
    policestation_password=models.CharField(max_length=40)
    policestation_photo=models.FileField(upload_to="Assets/Police/Photo/")
    policestation_proof=models.FileField(upload_to="Assets/Police/Proof")
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    police_status=models.IntegerField(default=0)

#advocate table
class tbl_advocate(models.Model):
    advocate_name=models.CharField(max_length=40)
    advocate_email=models.CharField(max_length=40)
    advocate_contact=models.CharField(max_length=40)
    advocate_address=models.CharField(max_length=40)
    advocate_password=models.CharField(max_length=40)
    advocate_photo=models.FileField(upload_to="Assets/Advocate/photo/")
    advocate_proof=models.FileField(upload_to="Assets/Advocate/photo")
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    advocate_status=models.IntegerField(default=0)


   







