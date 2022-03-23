from django.shortcuts import render,redirect
from .models import signup

# Create your views here.
def index(request):
    return render(request,'index.html')

def jquery(request):
    return render(request,'jqury.html')

def fb(request):
    return render(request,'fb.html')


# view to update and delete data from table signup
def main(request):
    data=signup.objects.all()
    if request.method=='POST':
        id=request.POST['id']
        obj=signup.objects.filter(signid=id)
        obj.delete()
    return render(request,'main.html',{'user':data})

# view to insert data into table signup
def form(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        pwd = request.POST['pwd']
        obj = signup(name=name, email=email, password=pwd)
        obj.save()

    return render(request,'form.html')

# view to update data into table signup
def update(request, id):
    obj = signup.objects.get(signid=id)
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        pwd = request.POST['pwd']
        obj.name = name
        obj.email = email
        obj.password = pwd
        obj.save()
    return render(request,'update.html',{'user':obj})


# login page setup
def login(request):
    msg=""
    if request.method=='POST':
        uname=request.POST['username']
        psw=request.POST['password']
        
        try:
            obj_exist=signup.objects.get(name=uname, password=psw)
            request.session['user']=obj_exist.signid
            return redirect("home")

        except signup.DoesNotExist:
            msg="Username or password incorrect"
    return render(request,"login.html",{'msg':msg,})

def home(request):
    obj=signup.objects.get(signid=request.session['user'])
    return render(request,"home.html",{'user':obj,})

def logout(request):
    del request.session['user']
    request.session.flush()

    return redirect("log_user")