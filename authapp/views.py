from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def signup(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']
        if password != confirm_password:
            messages.warning(request, 'password does not match')
            return redirect('signup')
        if len(password) < 8:
            messages.warning(request, 'password must be atleast 8 characters')

        try:
            if User.objects.get(email=email):
                messages.info(request, 'Email is Taken')

        except Exception as identifier:
            pass

        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        #user.is_active = True
        user.save()
        messages.success(request, f'{name} has been signed up successfully')
        return redirect('handle_login')
    else:
        messages.error(request, ' Password does not match')
    return render(request, 'signup.html')


def handle_login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['pass1']
        myuser = authenticate(username=username, password=password)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, 'Login Success')
            return redirect('index')
        else:
            messages.error(request, ' Invalid Credentials')
            return redirect('handle_login')
    return render(request, 'login.html')


def handle_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return render(request, 'login.html')
