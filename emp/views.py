from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate,login
from .models import Employee
from myapp.form import Loginform


# Create your views here.
def emp_home(request):
    emps=Employee.objects.all()
    return render(request,"emp/home.html",{"emps":emps})


class Login_user(View):
    def get(self,request):  
        log=Loginform()
        return render(request,"emp/Login.html",{"feed":log})

    def post(self,request):
        form=Loginform(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]   
            queryset= list(Employee.objects.values("name","empid"))
            for user in queryset:
                if user["name"]== username and user["empid"]==password:
                    return redirect("/emp/home")
# for admin user login....>>>>>    
    # user=authenticate(request,username=username,password=password)
        # if user is not None:
        #         login(request,user)
        #         return redirect("/emp/home")
            else:
                msg="login unsucessfull"
                log=Loginform()
                return render(request,"emp/Login.html",{"feed":log,"msg":msg})
        else:
            msg="form validation error!!! "
            log=Loginform()
            return render(request,"emp/Login.html",{"feed":log,"msg":msg})


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



    
