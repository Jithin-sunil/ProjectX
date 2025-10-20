from django.shortcuts import render,redirect
from Guest.models import *
from PoliceStation.models import *
from django.utils.timezone import now
from Advocate.models import *
import random
import string
# Create your views here.
def HomePage(request):
    return render(request,'PoliceStation/HomePage.html')
def Logout(request):
    del request.session['pid']
    return redirect("Guest:Login")
def myprofile(request):
    policedata=tbl_policestation.objects.get(id=request.session['pid'])
    return render(request,'PoliceStation/Myprofile.html',{'policedata':policedata})
def EditProfile(request):

        dis=tbl_district.objects.all()
        placename=tbl_place.objects.all()
        policedata=tbl_policestation.objects.get(id=request.session['pid'])
        if request.method=='POST':

                policestation_name=request.POST.get('txt_plcname')
                policestation_email=request.POST.get('txt_email')
                policestation_contact=request.POST.get('txt_contact')
                policestation_address=request.POST.get('txt_address')
                #advocate_password=request.POST.get('txt_password')
                policestation_photo=request.FILES.get('txt_photo')
                policestation_proof=request.FILES.get('txt_proof')
                place=tbl_place.objects.get(id=request.POST.get('sel_place'))
                policedata.policestation_name=policestation_name
                policedata.policestation_email=policestation_email
                policedata.policestation_contact=policestation_contact
                policedata.policestation_address=policestation_address
                policedata.policestation_photo=policestation_photo
                policedata.policestation_proof=policestation_proof
                policedata.place=place
                policedata.save()
                return render(request,'PoliceStation/EditProfile.html',{'msg':"updated"})
        else:

                return render(request,'PoliceStation/EditProfile.html',{'policedata':policedata,'dis':dis,'data':placename})


def changepwd(request):
        policedata=tbl_policestation.objects.get(id=request.session['pid'])
        dbpass=policedata.policestation_password
        if request.method=='POST':
                old=request.POST.get('txt_oldpwd')
                new=request.POST.get('txt_newpwd')
                cpass=request.POST.get('txt_confirmpwd')
                if dbpass==old:
                        if new==cpass:
                                policedata.policestation_password=new
                                policedata.save()
                                return render(request,'PoliceStation/Changepwd.html',{'msg':"password changed"})
                        else:
                                return render(request,'PoliceStation/Changepwd.html',{'msg':"password does not match"}) 
                else:
                        return render(request,{'msg':"invalid old password"})  
        else:
                return render(request,'PoliceStation/Changepwd.html') 
        
def Addcase(request):
    type = tbl_type.objects.all()
    case = tbl_case.objects.filter(policestation=request.session['pid'])

    if request.method == "POST":
      
        section = request.POST.get('txt_section')
        content = request.POST.get('txt_content')
        file = request.FILES.get('txt_file')
        ctype = tbl_type.objects.get(id=request.POST.get('sel_type'))
        police_station = tbl_policestation.objects.get(id=request.session['pid'])

        new_case = tbl_case.objects.create(
            case_number='TEMP', 
            case_section=section,
            case_content=content,
            case_file=file,
            type=ctype,
            policestation=police_station
        )

        date_str = now().strftime('%Y%m%d')  
        station_code = police_station.policestation_name[:3].upper()  
        random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))  
        case_id = new_case.id

        unique_case_number = f"{station_code}-{date_str}-{case_id:04d}-{random_part}"

        new_case.case_number = unique_case_number
        new_case.save()

        return render(request, 'PoliceStation/AddCase.html', {'msg': "Inserted Successfully.."})
    else:
        return render(request, 'PoliceStation/AddCase.html', {'type': type, 'case': case})

def casedelete(request,id):
       tbl_case.objects.get(id=id).delete()
       return redirect('PoliceStation:Addcase')


def viewrequest(request):
       reqdata=tbl_request.objects.filter(case__policestation=request.session['pid'])
       return render(request,"PoliceStation/ViewRequest.html",{'request':reqdata})


def verifyrequest(request,id,status):
       reqdata=tbl_request.objects.get(id=id)
       reqdata.request_status=status
       reqdata.save()
       return redirect('PoliceStation:viewrequest')
       