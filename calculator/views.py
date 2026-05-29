from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import calform
from calculator.models import Laptop
# Create your views here.

def Devices(request):
    if request.method=='POST':
        fn=calform(request.POST)
        if fn.is_valid():
            L_Name=request.POST.get('Name')
            L_Desc=request.POST.get('Description')
            form_data=Laptop(Laptop_name=L_Name,Laptop_desc=L_Desc,Laptop_img=None)
            form_data.save()
            return redirect('Laptop_data')

        else:
            print(fn.errors)
    else:
        fn=calform()

    L_data=Laptop.objects.all().order_by('id')
    data={
        'form':fn,
        'L_data':L_data,
    }
    return render(request,"index.html",data)

def calculator(request):
    fn=calform()
    data={
        'form':fn,
    }
    # try : 
    #     if request.method == "POST":
    #         if calform.opr=="add":
    #             result=calform.num1+calform.num2
    #         elif calform.opr=="sub":
    #             result=calform.num1-calform.num2
    #         elif calform.opr=="mult":
    #             result=calform.num1*calform.num2
    #         elif calform.opr=="div":
    #             result=calform.num1/calform.num2
    #         elif calform.opr=="mod":
    #             result=calform.num1%calform.num2
    #         elif calform.opr=="pow":
    #             result=calform.num1**calform.num2
    # except:
    #     result='invalid'

    # data.update(result)
    return render(request,"index.html",data)

def res(request):
    result=0
    if request.method == "POST":
        try : 
            num1=int(request.POST.get('num1'))
            num2=int(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="add":
                result=num1+num2
            elif opr=="sub":
                result=num1-num2
            elif opr=="mul":
                result=num1*num2
            elif opr=="div":
                result=num1/num2
            elif opr=="mod":
                result=num1%num2
            elif opr=="pow":
                result=num1**num2
        except Exception as e:
            print(f"Error occurred: {e}")
            result = -1
        
    return render(request,"result.html",{'result':result})