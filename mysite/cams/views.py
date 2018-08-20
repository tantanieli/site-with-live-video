from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http.response import HttpResponse


def index(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    cameras = request.user.camera_set.all()
    if cameras.count() == 0:
        return HttpResponse("У вас пока нет доступа ни к одной камере")
    return render(request, 'index.html', context={'cameras': cameras})


def enter(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('/')
    else:
        return render(request, 'login.html')
