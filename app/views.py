from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login , logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')
def SignupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        v_password = request.POST.get('v_password')
        if password != v_password:
            print(123)
            messages.warning(request, ('Your password and confirm password are not equal'))
            return render(request,'signup.html')
        print(456)
        user = User.objects.create_user(username,email,password)
        user.save()
        messages.success(request, ('Thank you'))
        return redirect('login')
    else:
        return render(request,'signup.html')
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)
        if user:
            print(123)
            login(request,user)
            return redirect('home')
        
    return render(request,'login.html')

def Logout(request):
    logout(request)
    return redirect('login')