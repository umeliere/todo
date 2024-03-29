from django.shortcuts import render, redirect
from users.forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout, authenticate


def registration(request):
    """
    Registration view
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            form.add_error('__all__', 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'users/registration.html', {'form': form})


def user_login(request):
    """
    Login view
    """
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST['next'])
                return redirect('home')
            else:
                form.add_error('__all__', 'Учетная запись пользователя не найдена')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    """
    Logout view
    """
    logout(request)
    return redirect('home')
