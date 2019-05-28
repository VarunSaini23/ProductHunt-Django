from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'],
                                 password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username or Password not correct'})

    else:
        return render(request, "accounts/login.html")


def signup(request):
    if request.method == "POST":
        # TODO : signupUser
        print(request.POST['password1'])
        print(request.POST['username'])
        print("hello world")
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, "accounts/signup.html", {'error': "Username already exists"})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST["username"], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, "accounts/signup.html", {'error': "Password Dont Match"})
    else:
        # TODO : show login form
        return render(request, "accounts/signup.html")


def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')