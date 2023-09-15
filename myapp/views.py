from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,'home.html')

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('Pass2')

        user = User.objects.create_user(username,email,pass1)
        user.first_name=fname
        user.last_name=lname
        user.save()
        messages.success(request,"your account has been succesfully created")
        return redirect('login')
        
    return render(request,'authentication/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user1 = authenticate(username = username ,password = pass1)

        if user1 is not None:
            login(request, user1)
            fname = user1.first_name
            messages.success(request,"you've logged in succesfully")
            return render(request,"index.html",{'fname':fname})
        
        else:
            messages.error(request,"bad credentials")
            return redirect('login')
        
    return render(request,'authentication/login.html')

def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request,"Successfully logged out")