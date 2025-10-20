from django.shortcuts import render,redirect
from Admin.models import*
from Advocate.models import*
from Guest.models import*
from PoliceStation.models import *
from User.models import *
from datetime import datetime
from django.db.models import Q
# Create your views here.
def HomePage(request):
        return render(request,'Advocate/HomePage.html')

def Logout(request):
    del request.session['advid']
    return redirect("Guest:Login")

def MyProfile(request):
        advdata=tbl_advocate.objects.get(id=request.session['advid'])
        return render(request,'Advocate/MyProfile.html',{'advdata':advdata})
def EditProfile(request):

        dis=tbl_district.objects.all()
        placename=tbl_place.objects.all()
        advdata=tbl_advocate.objects.get(id=request.session['advid'])
        if request.method=='POST':

                advocate_name=request.POST.get('txt_advname')
                advocate_email=request.POST.get('txt_email')
                advocate_contact=request.POST.get('txt_contact')
                advocate_address=request.POST.get('txt_address')
                #advocate_password=request.POST.get('txt_password')
                advocate_photo=request.FILES.get('txt_photo')
                advocate_proof=request.FILES.get('txt_proof')
                advocate_place=tbl_place.objects.get(id=request.POST.get('sel_place'))
                advdata.advocate_name=advocate_name
                advdata.advocate_email=advocate_email
                advdata.advocate_contact=advocate_contact
                advdata.advocate_address=advocate_address
                advdata.advocate_photo=advocate_photo
                advdata.advocate_proof=advocate_proof
                advdata.place=advocate_place
                advdata.save()
                return render(request,'Advocate/EditProfile.html',{'msg':"updated"})
        else:

                return render(request,'Advocate/EditProfile.html',{'advdata':advdata,'dis':dis,'data':placename})

def changepwd(request):
        advocatedata=tbl_advocate.objects.get(id=request.session['advid'])
        dbpass=advocatedata.advocate_password
        if request.method=='POST':
                old=request.POST.get('txt_oldpwd')
                new=request.POST.get('txt_newpwd')
                cpass=request.POST.get('txt_confirmpwd')
                if dbpass==old:
                        if new==cpass:
                                advocatedata.advocate_password=new
                                advocatedata.save()
                                return render(request,'Advocate/ChangePassword.html',{'msg':"password changed"})
                        else:
                                return render(request,'Advocate/ChangePassword.html',{'msg':"password does not match"}) 
                else:
                        return render(request,{'msg':"invalid old password"})  
        else:
                return render(request,'Advocate/ChangePassword.html')              


def ViewBooking(request):
        bookdata=tbl_booking.objects.all()
        return render(request,'Advocate/ViewBooking.html',{'bookdata':bookdata})

        
def verifybooking(request,id,status):
        bookingdata=tbl_booking.objects.get(id=id)
        bookingdata.booking_status=status
        bookingdata.save()
        return redirect('Advocate:ViewBooking')


def viewstation(request):
       policestation=tbl_policestation.objects.filter(police_status=1)
       return render(request,'Advocate/ViewPoliceStation.html',{'policedata':policestation})

def viewcase(request, id):
    if request.method == "POST":
        policestation = tbl_policestation.objects.get(id=id)
        case = tbl_case.objects.get(
            case_number=request.POST.get("txt_casenum"),
            policestation=policestation
        )
        return render(request, "Advocate/ViewCase.html", {'case': case})
    else:
        return render(request, "Advocate/ViewCase.html")

       
def sendrequest(request,id):
       if request.method == "POST":
              reqdec=request.POST.get("txt_desc")
              case=tbl_case.objects.get(id=id)
              advocate=tbl_advocate.objects.get(id=request.session['advid'])
              tbl_request.objects.create(request_casedesc=reqdec,case=case,advocate=advocate)
              return render(request,"Advocate/SendRequest.html",{'msg':"Request Sended.."})
       else:
              return render(request,"Advocate/SendRequest.html")
              

def myrequest(request):
       reqdata=tbl_request.objects.filter(advocate=request.session['advid'])
       return render(request,"Advocate/MyRequest.html",{'request':reqdata})

def casedetails(request,id):
        case=tbl_case.objects.get(id=id)
        return render(request,"Advocate/CaseDetails.html",{'case':case})


def sendbail(request,id):
        if request.method=="POST":
                bailfile=request.FILES.get("txt_bailfile")
                reqdata=tbl_request.objects.get(id=id)
                reqdata.request_bailfile=bailfile
                reqdata.request_status=3
                reqdata.save()
                return render(request,"Advocate/SendBail.html",{'msg':"Bail Sent Successfully.."})
        else:
                return render(request,"Advocate/SendBail.html")

def chatpage(request,id):
    user  = tbl_user.objects.get(id=id)
    return render(request,"Advocate/Chat.html",{"user":user})

def ajaxchat(request):
    from_advocate = tbl_advocate.objects.get(id=request.session["advid"])
    to_user = tbl_user.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),advocate_from=from_advocate,user_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"Advocate/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    advocate = tbl_advocate.objects.get(id=request.session["advid"])
    chat_data = tbl_chat.objects.filter((Q(advocate_from=advocate) | Q(advocate_to=advocate)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"Advocate/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(advocate_from=request.session["advid"]) & Q(user_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(advocate_to=request.session["uid"]))).delete()
    return render(request,"Advocate/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})