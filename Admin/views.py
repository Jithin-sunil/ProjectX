from django.shortcuts import render,redirect
from Admin.models import*
from User.models import*
from Guest.models import*
from Advocate.models import*
from PoliceStation.models import*

#adminfeild
def Logout(request):
    del request.session['aid']
    return redirect('Guest:Login')

def Homepage(request):
    total_users = tbl_user.objects.count()
    total_advocates = tbl_advocate.objects.count()
    total_police = tbl_policestation.objects.count()
    total_cases = tbl_request.objects.count()
    total_bookings = tbl_booking.objects.count()
    total_complaints = tbl_complaint.objects.count()

   
    recent_bookings = (
        tbl_booking.objects.select_related('user', 'advocate')
        .order_by('-id')[:5]
    )
    recent_complaints = (
        tbl_complaint.objects.select_related('user')
        .order_by('-id')[:5]
    )
    top_advocates = tbl_advocate.objects.all()[:4]

    context = {
        'total_users': total_users,
        'total_advocates': total_advocates,
        'total_police': total_police,
        'total_cases': total_cases,
        'total_bookings': total_bookings,
        'total_complaints': total_complaints,
        'recent_bookings': recent_bookings,
        'recent_complaints': recent_complaints,
        'top_advocates': top_advocates,
    }

    return render(request, 'Admin/Homepage.html', context)
    

def Admin(request):
    admindata=tbl_admin.objects.all()
    if request.method=='POST':
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        password=request.POST.get('txt_password')

        tbl_admin.objects.create(admin_name=name,admin_email=email,admin_password=password)
        return render(request,'Admin/Admin.html',{'msg':"insertion successful"})
    else:
        return render(request,'Admin/Admin.html',{'data':admindata})

def deladmin(request,did):
    tbl_admin.objects.get(id=did).delete()
    # return redirect('Admin:Admin')
    return render(request,'Admin/Admin.html',{'msg':"Deleted"})

def editadmin(request,eid):
    editdata=tbl_admin.objects.get(id=eid)
    if  request.method=='POST':
        name= request.POST.get('txt_name')
        email= request.POST.get('txt_email')
        password= request.POST.get('txt_password')
        editdata.admin_name=name
        editdata.admin_email=email
        editdata.admin_password=password
        editdata.save()
        return render(request,'Admin/Admin.html',{'msg':"updated"})
    else:
        return render(request,'Admin/Admin.html',{'editdata':editdata})  

#type
def type(request):
    data=tbl_type.objects.all()
    if request.method=='POST':
        name=request.POST.get('txt_type')
        tbl_type.objects.create(type_name=name)
        return render(request,'Admin/Type.html',{'msg':"Data Submitted"})
    else:
        return render(request,'Admin/Type.html',{'type':data})
       
#deltype
def deletetype(request,id):
    tbl_type.objects.get(id=id).delete()
    return redirect('Admin:type')

#edittype
def edittype(request,id):
    data=tbl_type.objects.all()
    editdata=tbl_type.objects.get(id=id)
    if request.method=='POST':
        editdata.type_name=request.POST.get('txt_type')
        editdata.save()
        return render(request,'Admin/Type.html',{'msg':"Data Updated"})
    else:
        return render(request,'Admin/Type.html',{'type':data,'editdata':editdata})

#district feild
    
def District(request):
    Ddata=tbl_district.objects.all()
    if request.method=='POST':
        district_name= request.POST.get('txt_DistrictName')
        tbl_district.objects.create(district_name=district_name)
        return render(request,'Admin/District.html',{'msg':"Inserted"})
    else:
        return render(request,'Admin/District.html',{'dis':Ddata})
    
def deldistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return render(request,'Admin/District.html',{'msg':"Deleted"})
    
def editdistrict(request,eid):
    editdata=tbl_district.objects.get(id=eid)
    if request.method=='POST':
        name= request.POST.get('txt_DistrictName')
        editdata.district_name=name
        editdata.save()
        return render(request,'Admin/District.html',{'msg':"Updated"})
    else:
        return render(request, 'Admin/District.html',{'editdata':editdata})


#place fields

def Place(request):
    disdata=tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    if request.method=='POST':
        district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        place=request.POST.get('Place')

        tbl_place.objects.create(place_name=place,district=district)
        return render(request,'Admin/Place.html',{'msg':"Inserted"})
    else:
        return render(request ,'Admin/Place.html',{'dis':disdata,'places':placedata})

def delplace(request,pid):
    tbl_place.objects.get(id=pid).delete()
    return render(request,'Admin/Place.html',{'msg':"Deleted"})

def editplace(request,peid):
    disdata=tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    editdata=tbl_place.objects.get(id=peid)
    if request.method=='POST':
        district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        place=request.POST.get('Place')

        editdata.place_name=place
        editdata.district=district
        editdata.save()
        return render(request,'Admin/Place.html',{'msg':"Updated"})
    else:
        return render(request ,'Admin/Place.html',{'dis':disdata,'places':placedata,'editdata':editdata})
def viewadvocates(request):
    advnew=tbl_advocate.objects.filter(advocate_status=0)
    advver=tbl_advocate.objects.filter(advocate_status=1)
    advrej=tbl_advocate.objects.filter(advocate_status=2)
    return render(request ,'Admin/ViewAdvocates.html',{'adv':advnew,'advver':advver,'advrej':advrej})

def acceptadvocates(request,aid):
    data=tbl_advocate.objects.get(id=aid)
    data.advocate_status=1
    data.save()
    return render(request ,'Admin/ViewAdvocates.html',{'msg':"Verified"})

def rejectadvocates(request,rid):
    data=tbl_advocate.objects.get(id=rid)
    data.advocate_status=2
    data.save()
    return render(request ,'Admin/ViewAdvocates.html',{'msg':"Rejected"})


def viewpolicestation(request):
    policenew=tbl_policestation.objects.filter(police_status=0)
    policever=tbl_policestation.objects.filter(police_status=1)
    policerej=tbl_policestation.objects.filter(police_status=2)
    return render(request ,'Admin/PolicestationVerification.html',{'police':policenew,'policever':policever,'policerej':policerej})

def acceptstation(request,aid):
    data=tbl_policestation.objects.get(id=aid)
    data.police_status=1
    data.save()
    return render(request ,'Admin/PolicestationVerification.html',{'msg':"Verified"})

def rejectstation(request,rid):
    data=tbl_policestation.objects.get(id=rid)
    data.police_status=2
    data.save()
    return render(request ,'Admin/PolicestationVerification.html',{'msg':"Rejected"})

def viewcomplaints(request):
    complaints=tbl_complaint.objects.filter(complaint_status=0)
    replied=tbl_complaint.objects.filter(complaint_status=1)
    return render(request,'Admin/ViewComplaint.html',{'complaints':complaints,'replied':replied})
def replycomplaint(request,cid):
    complaintdata=tbl_complaint.objects.get(id=cid)
    if request.method=='POST':
        reply=request.POST.get('txt_reply')
        complaintdata.complaint_reply=reply
        complaintdata.complaint_status=1
        complaintdata.save()
        return render(request,'Admin/ReplyComplaint.html',{'msg':"Replied"})
    else:
        return render(request,'Admin/ReplyComplaint.html',{'complaintdata':complaintdata})