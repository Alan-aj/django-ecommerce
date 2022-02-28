from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')


def main(request):
    return render(request,'main.html')

def jquery(request):
    return render(request,'jqury.html')

def form(request):
    return render(request,'form.html')

def fb(request):
    return render(request,'fb.html')