from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login as ulogin,logout as ulogout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from user_profile.models import UserProfile


def index(request):
    return render(request, 'index.html')

def signin(request):
    return render(request, 'SignIn.html')

def login(request):
    if not request.user.is_authenticated:
        return render(request,"login.html")
    if request.method=='POST':
        uname=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        mobno=request.POST['mobno']
        gender=request.POST['gender']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        age=request.POST['age']
        address=request.POST['address']
        email=request.POST['email']
        myuser=User.objects.create_user(uname,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        extrainfo=UserProfile(user_id=myuser.id,phone=mobno, gender=gender, age=age, address=address)
        extrainfo.save()
        myuser.save()
    return render(request, 'login.html')


def logout(request):
    ulogout(request)
    return redirect('login')


def filter(request):
    return render(request, 'filter.html')


def home(request):
    allprofile=UserProfile.objects.all()
    if request.method=='POST':
        range1=0
        range2=46
        age1=request.POST.get('age1', 'off')
        age2=request.POST.get('age2', 'off')
        age3=request.POST.get('age3', 'off')
        age4=request.POST.get('age4', 'off')
        if(age4=='on'):
            range1=45
            range2=100
            for user in allprofile:
                print(user)
        if(age3=='on'):
            range1=35
        if(age2=='on'):
            range1=25
        if(age1=='on'):
            range1=15
        male=request.POST.get('male','off')
        female=request.POST.get('other','off')
        other=request.POST.get('other','off')
        other=request.POST.get('other','off')
        shark1=request.POST.get('shark1','off')
        shark2=request.POST.get('shark2','off')
        shark3=request.POST.get('shark3','off')
        shark4=request.POST.get('shark4','off')
        shark5=request.POST.get('shark5','off')
        shark6=request.POST.get('shark6','off')
        shark7=request.POST.get('shark7','off')
        shark8=request.POST.get('shark8','off')
        shark9=request.POST.get('shark9','off') 
        shark10=request.POST.get('shark10','off')
        shark11=request.POST.get('shark11','off')
        shark12=request.POST.get('shark12','off')
    return render(request, 'home.html')