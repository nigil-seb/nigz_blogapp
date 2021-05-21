from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth,User
# Create your views here.
from blogapp.models import Blogs


def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exist   :(')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exist  :(')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save();
                print('Registration successful, account created!')
        else:
            print('##password not matching##')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'registration.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid details')
            return redirect('login')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')