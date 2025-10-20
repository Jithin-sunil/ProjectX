from django.shortcuts import render

# Create your views here.
def Add(request):
    return render(request,'Basics/Add.html')
def Cal(request):
    sum=""
    res=""
    c=""
    div=""
    if request.method=='POST':
        num1=int(request.POST.get('FirstNumber'))
        num2=int(request.POST.get('SecondNumber'))
        but=request.POST.get('button')
        if but=='add':
            sum=num1+num2
        elif but=='sub':
            res=num1-num2
        elif but=='mult':
            c=num1*num2
        else:
            div=num1/num2
        return render(request,'Basics/Calc.html',{'a':sum,'b':res,'c':c,'d':div})
    else:
        return render(request,'Basics/Calc.html')
