from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html', {})


def cambiar_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Su password fue actualizado correctamente!')
            return redirect('core:index')
        else:
            messages.error(request, 'Por favor corriga el error.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'core/password_update_form.html', {
        'form': form
    })


def info_demo(request):
    return render(request, 'core/demo.html', {})


def info_sitio(request):
    return render(request, 'core/info.html', {})
