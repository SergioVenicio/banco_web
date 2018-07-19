from . import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


def sign_up(request):
    if request.method == 'POST':
        form = forms.UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = forms.UserForm()
    context = {'form': form}
    return render(request, 'registration/signup.html', context)


@login_required(login_url='/login')
def home(request):
    return render(request, 'home.html')
