from django.shortcuts import render,redirect
from django.views import View
from emp.models import Employee

def home(request):
    return render(request,"index.html")


class Registration(View):
    def get(self,request):
        return render(request,"registration.html",{})
    
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
        msg="""You are registered sucessfully!!
                You can now login"""
        return render(request,"registration.html",{"msg":msg})  


