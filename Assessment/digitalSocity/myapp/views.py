from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    msg=''
    if request.method=='POST':
        form=signupForm(request.POST)
        if form.is_valid():
            pas=request.POST['password']
            cpas=request.POST['cpassword']
            if pas==cpas:
                form.save()
                print('Signup Successfully!')
            else:
                msg='Password Not Match'
        else:
            print(form.errors)
    else:
        form = signupForm()
    return render(request,'signup.html',{'form':form})

def verifyotp(request):
    return render(request,'verifyotp.html')

def invoice(request):
    return render(request,'invoice.html')

def notice(request):
    return render(request,'notice.html')

def event(request):
    return render(request,'event.html')

def societymember(request):
    return render(request,'societymember.html')

def watchman(request):
    return render(request,'watchman.html')

def profile(request):
    return render(request,'profile.html')