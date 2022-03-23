from django.shortcuts import render
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