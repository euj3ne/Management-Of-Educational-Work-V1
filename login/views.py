from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


def login_(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('panel/')
        else:
            error_message = "Неправильный пароль или имя пользователя."
            data = {'error_message': error_message}
            return render(request, 'login/index.html', data)
    return render(request, 'login/index.html')

def logout_(request):
    logout(request)
    return redirect(reverse('login:login'))