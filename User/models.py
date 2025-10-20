from django.db import models
from Guest.models import*

# Create your models here.
class tbl_booking(models.Model):
    booking_date= models.DateField(auto_now_add=True)
    booking_status=models.IntegerField(default=0)
    booking_content=models.CharField(max_length=150)
    booking_file=models.FileField(upload_to="Assets/User/file")
    booking_amount=models.CharField(max_length=40)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    advocate=models.ForeignKey(tbl_advocate,on_delete=models.CASCADE)


class tbl_chat(models.Model):
    
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user_from = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_from",null=True)
    user_to = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_to",null=True)
    advocate_from = models.ForeignKey(tbl_advocate,on_delete=models.CASCADE,related_name="advocate_from",null=True)
    advocate_to = models.ForeignKey(tbl_advocate,on_delete=models.CASCADE,related_name="advocate_to",null=True)

class tbl_complaint(models.Model):
    complaint_date=models.DateField(auto_now_add=True)
    complaint_title=models.CharField(max_length=150)
    complaint_content=models.CharField(max_length=500)
    complaint_status=models.IntegerField(default=0)
    complaint_reply=models.CharField(max_length=500,null=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)