from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from learning_center.models import StudentModel
from .forms import Signup_form, LoginForm
from django.contrib.auth import login, authenticate, logout

from .models import CustomUser


def registration_view(request):
    form = Signup_form()
    # print(form)
    if request.method == 'POST':
        form = Signup_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            del form.cleaned_data['confirm_password']
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            usr = CustomUser.objects.all()[::-1]
            id = usr[0]
            a1 = StudentModel.objects.create(student=id)
            print(a1, "ohirgi user ")

            return redirect('login')

    return render(request, 'registration.html', context={
        'form': form
    })


def login_view(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            user = authenticate(
                username=forms.cleaned_data['username'],
                password=forms.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            forms.add_error('password', 'Parol yoki username noto\'g\'ri !')

    return render(request, 'login.html', context={
        "form": forms
    })


def logout_view(request):
    logout(request)
    return redirect('login')
