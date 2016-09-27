from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.


def index(request):
    return render(request, "landr/index.html")


def register(request):
    if request.method=="POST":
        reg_data = User.objects.new_user(request.POST)
        if reg_data['created']:
            messages.success(request, "{} successfully registered".format(reg_data['new_user'].name))
        else:
            for error in reg_data['errors']:
                messages.error(request, error)
    return redirect('landr:index')


def login(request):
    if request.method == "POST":
        user = User.objects.login(request.POST)
        if user['log_in']:
            request.session['user_id'] = user['user'].id
            request.session['user_name'] = user['user'].name
            return redirect('wishlist:index')
        else:
            for error in user['errors']:
                messages.error(request, error)
            return redirect('landr:index')


def logout(request):
    request.session.clear()
    return redirect("landr:index")
