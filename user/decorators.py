
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

def admin_required(function):
    def wrap(request, *args, **kwargs):
        instance = request.user
        if instance.is_staff == True or instance.is_superuser == True:
            return function(request, *args, **kwargs)
        else:
            messages.warning(request, f'You are not authorized to acess this page!')
            return redirect('home')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

