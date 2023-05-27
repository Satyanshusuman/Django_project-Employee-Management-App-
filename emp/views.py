from django.shortcuts import render,redirect
from django.views import View
from .models import Employee

# Create your views here.
def emp_home(request):
    emps=Employee.objects.all()
    return render(request,"emp/home.html",{"emps":emps})

class Registration(View):
    def get(self,request):
        return render(request,"emp/registration.html",{})
    
    def post(self,request):
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_department=request.POST.get("emp_department")
        emp_add=request.POST.get("emp_add")
        emp_working=request.POST.get("emp_working")
        e=Employee()
        e.name=emp_name
        e.empid=emp_id
        e.phone=emp_phone
        e.address=emp_add
        e.departments=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()
        return redirect("/emp/home")  
   
class Update(View):

    def get(self,request,id):
        emp=Employee.objects.get(pk=id)
        return render (request,"emp/update.html",{"emp":emp})
    
    def post(self,request,id):
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_department=request.POST.get("emp_department")
        emp_add=request.POST.get("emp_add")
        emp_working=request.POST.get("emp_working")
        
        e=Employee.objects.get(pk=id)
        e.name=emp_name
        e.empid=emp_id
        e.phone=emp_phone
        e.address=emp_add
        e.departments=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()
        return redirect("/emp/home")
   
def delete(request,id):
    e=Employee.objects.get(pk=id)
    e.delete()
    return redirect("/emp/home")



    
