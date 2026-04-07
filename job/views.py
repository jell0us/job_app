from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_user(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('dashboard')
        
        return render(request, 'login.html')
    
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid password or username')
            return redirect('login_user')

# Create your views here.
