from django.shortcuts import render,redirect
from Guest.models import*
from User.models import *
from datetime import datetime
from django.db.models import Q
# Create your views here.
def HomePage(request):
    return render(request,'User/HomePage.html')
def Logout(request):
    del request.session['uid']
    return redirect("Guest:Login")
def myprofile(request):
    userdata=tbl_user.objects.get(id=request.session['uid'])
    return render(request,'User/Myprofile.html',{'userdata':userdata})

def EditProfile(request):
    dis=tbl_district.objects.all()
    placename=tbl_place.objects.all()
    userdata=tbl_user.objects.get(id=request.session['uid'])
    if request.method=='POST':
        user_name=request.POST.get('txt_username')
        user_email=request.POST.get('txt_email')
        user_contact=request.POST.get('txt_contact')
        user_address=request.POST.get('txt_address')
        user_photo=request.FILES.get('txt_photo')
     
        place=tbl_place.objects.get(id=request.POST.get('sel_place'))
        userdata.user_name=user_name
        userdata.user_email=user_email
        userdata.user_contact=user_contact
        userdata.user_address=user_address
        userdata.user_photo=user_photo
        
        userdata.place=place
        userdata.save()
        return render(request,'User/EditProfile.html',{'msg':"updated"})
    else:

        return render(request,'User/EditProfile.html',{'userdata':userdata,'dis':dis,'data':placename})

def changepwd(request):
        userdata=tbl_user.objects.get(id=request.session['uid'])
        dbpass=userdata.user_password
        if request.method=='POST':
                old=request.POST.get('txt_oldpwd')
                new=request.POST.get('txt_newpwd')
                cpass=request.POST.get('txt_confirmpwd')
                if dbpass==old:
                        if new==cpass:
                                userdata.policestation_password=new
                                userdata.save()
                                return render(request,'User/Changepwd.html',{'msg':"password changed"})
                        else:
                                return render(request,'User/Changepwd.html',{'msg':"password does not match"}) 
                else:
                        return render(request,{'msg':"invalid old password"})  
        else:
                return render(request,'User/Changepwd.html')     
    



def viewadvocates(request):
    adv=tbl_advocate.objects.all()
    return render(request ,'User/Viewadvocates.html',{'adv':adv})

def booking(request,lawid):
    advocate=tbl_advocate.objects.get(id=lawid)
    user=tbl_user.objects.get(id=request.session['uid'])
    tbl_booking.objects.create(advocate=advocate,user=user)
    return render(request,'User/Viewadvocates.html',{'msg':"Booking Successful"})


def viewbooking(request):
      bookdata=tbl_booking.objects.filter(user=request.session['uid'])
      return render(request,'User/Mybooking.html',{'bookdata':bookdata})


def uploaddocs(request,bid):
    bookingdata=tbl_booking.objects.get(id=bid)
    if request.method=='POST':
        booking_docs=request.FILES.get('docfile')
        booking_content=request.POST.get('description')
        bookingdata.booking_content=booking_content
        bookingdata.booking_file=booking_docs
        bookingdata.booking_status=3
        bookingdata.save()
        return redirect('User:viewbooking')
    else:
        return render(request,'User/UploadDocs.html')


def chatpage(request,id):
    advocate  = tbl_advocate.objects.get(id=id)
    return render(request,"User/Chat.html",{"user":advocate})

def ajaxchat(request):
    from_user = tbl_user.objects.get(id=request.session["uid"])
    to_advocate = tbl_advocate.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,advocate_to=to_advocate,chat_file=request.FILES.get("file"))
    return render(request,"User/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_user.objects.get(id=request.session["uid"])
    chat_data = tbl_chat.objects.filter((Q(user_from=user) | Q(user_to=user)) & (Q(advocate_from=tid) | Q(advocate_to=tid))).order_by('chat_time')
    return render(request,"User/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(user_from=request.session["uid"]) & Q(advocate_to=request.GET.get("tid")) | (Q(advocate_from=request.GET.get("tid")) & Q(advocate_to=request.session["uid"]))).delete()
    return render(request,"User/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})


def complaint(request):
    complaints=tbl_complaint.objects.filter(user=request.session['uid'])
    if request.method=='POST':
        complaint_title=request.POST.get('txt_title')
        complaint_content=request.POST.get('txt_content')
        user=tbl_user.objects.get(id=request.session['uid'])
        tbl_complaint.objects.create(complaint_title=complaint_title,complaint_content=complaint_content,user=user)
        return render(request,'User/Complaint.html',{'msg':"Complaint Submitted"})
    else:
        return render(request,'User/Complaint.html',{'complaints':complaints})

def delete_complaint(request,cid):
    complaint=tbl_complaint.objects.get(id=cid)
    complaint.delete()
    return redirect('User:complaint')