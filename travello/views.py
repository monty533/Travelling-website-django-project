from django.shortcuts import render, redirect , HttpResponse
from .models import Destination
from django.contrib.auth.models import User 
from django.contrib.auth import logout , authenticate , login
from django.contrib import messages


# Create your views here.
def about_view(request):
    return render(request,'travello/about.html')

def cities_view(request):
    return render(request,'travello/cities.html')

def index_view(request):

    dests = Destination.objects.all()
    # dests = Destination.objects.filter(name='Delhi')

    return render(request, 'travello/index.html',{'dests':dests})

def register_view(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if (password1==password2): # same
            if User.objects.filter(username=username).exists(): # same 1
                # print('Username taken')  # same 1
                messages.success(request,'Username taken')
                return redirect('Register')

            elif User.objects.filter(email=email).exists():  # same 1   
                # print('email taken')   # same 1
                messages.info(request,'email taken')
                return redirect('Register')

            else:  # same 1
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                # print('user created')
                return redirect('Login')
            
        else: # same
            # print('password not matchting...') # same
            messages.info(request,'password not matching')
            return redirect('Register')

        return redirect('/')
    else:
        return render(request, 'travello/register.html')

def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request , user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials, try again')
            return redirect('Login')

    else:    
        return render(request, 'travello/login.html')
    
def logout_view(request):
    logout(request)
    return redirect('/')
