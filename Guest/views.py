from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
# Create your views here.

def index(request):
    return render(request,'Guest/index.html')

def Login(request):
    if request.method=='POST':
        email=request.POST.get('txt_email')
        password=request.POST.get('txt_password')

        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        policecount=tbl_policestation.objects.filter(policestation_email=email,policestation_password=password).count()
        advocatecount=tbl_advocate.objects.filter(advocate_email=email,advocate_password=password).count()


        if usercount>0:
            userdata=tbl_user.objects.get(user_email=email,user_password=password)
            request.session['uid']=userdata.id
            return redirect('User:HomePage')
        elif policecount>0:
            policedata=tbl_policestation.objects.get(policestation_email=email,policestation_password=password)
            request.session['pid']=policedata.id
            return redirect('PoliceStation:HomePage')
        elif advocatecount>0:
            advocatedata=tbl_advocate.objects.get(advocate_email=email,advocate_password=password)
            request.session['advid']=advocatedata.id
            return redirect('Advocate:HomePage')      
        else:
            return render(request,'Guest/Login.html',{'msg':"Invalid Login"})
    else:
        return render(request,'Guest/Login.html')

def Ajaxplace(request):
    place=tbl_place.objects.filter(district=request.GET.get('disid'))
    return render(request,"Guest/Ajaxplace.html",{'data':place})

def policereg(request):
    district=tbl_district.objects.all()
    if request.method=='POST':
        name=request.POST.get('txt_policestation')
        policestation_email=request.POST.get('txt_email')
        policestation_contact=request.POST.get('txt_contact')
        policestation_address=request.POST.get('txt_address')
        policestation_password=request.POST.get('txt_password')
        policestation_photo=request.FILES.get('txt_photo')
        policestation_proof=request.FILES.get('txt_proof')
        policestation_place=tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_policestation.objects.create(policestation_name=name,policestation_email=policestation_email,policestation_contact=policestation_contact,policestation_address=policestation_address,policestation_password=policestation_password,policestation_photo=policestation_photo,policestation_proof=policestation_proof,place=policestation_place)
        return render(request,'Guest/PoliceRegistration.html',{'msg':"Inserted Successfully"})
    else:
        

        return render(request,"Guest/PoliceRegistration.html",{'dis':district})
def advocatereg(request):
    district=tbl_district.objects.all()
    if request.method=='POST':
        advocate_name=request.POST.get('txt_advname')
        advocate_email=request.POST.get('txt_email')
        advocate_contact=request.POST.get('txt_contact')
        advocate_address=request.POST.get('txt_address')
        advocate_password=request.POST.get('txt_password')
        advocate_photo=request.FILES.get('txt_photo')
        advocate_proof=request.FILES.get('txt_proof')
        advocate_place=tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_advocate.objects.create(advocate_name=advocate_name,advocate_email=advocate_email,advocate_contact=advocate_contact,advocate_address=advocate_address,advocate_password=advocate_password,advocate_photo=advocate_photo,advocate_proof=advocate_proof,place=advocate_place)
        return render(request,'Guest/AdvocateRegistration.html', {'msg':"inserted successfully"})
    else:
        return render(request,'Guest/AdvocateRegistration.html',{'dis':district})
    
def Userreg(request):
    district=tbl_district.objects.all()
    if request.method=='POST':
        user_name=request.POST.get('txt_username')
        user_email=request.POST.get('txt_email')
        user_contact=request.POST.get('txt_contact')
        user_address=request.POST.get('txt_address')
        user_gender=request.POST.get('txt_Gender')
        user_photo=request.FILES.get('txt_photo')
        user_password=request.POST.get('txt_password')
        place=tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_user.objects.create(user_name=user_name,user_email=user_email,user_contact=user_contact,user_address=user_address,user_gender=user_gender,user_photo=user_photo,user_password=user_password,place=place)
        return render(request,'Guest/UserRegistration.html')
    else:
        return render(request,'Guest/UserRegistration.html',{'dis':district})
        
           



        
            
        