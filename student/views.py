from django.contrib.auth import authenticate, login
from django.shortcuts import  redirect, render



def user_login(request):
    if request.method == 'POST':
        cd = request.POST
        user = authenticate(username=cd['username'], password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
        else:
            message = 'Incorrect login/password or user not exist'
            return render(request, 'login/index.html', {'error':message})
    else:
        return render(request, 'login/index.html')


