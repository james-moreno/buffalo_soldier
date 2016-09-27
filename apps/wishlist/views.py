from django.shortcuts import render, redirect
from django.contrib import messages
from ..landr.models import User
from .models import Item

# Create your views here.
def index(request):
    context = {
    "my_products": Item.objects.filter(created_by=request.session['user_name']),
    "other_products": Item.objects.exclude(created_by=request.session['user_name']),
    }
    return render(request, 'wishlist/index.html', context)


def add_item(request):
    return render(request, 'wishlist/add_item.html')


def create(request):
    if request.method == "POST":
        creator = request.session['user_name']
        create_data = Item.objects.new_item(request.POST, creator)
        if create_data['created']:
            return redirect('wishlist:index')
        else:
            for error in create_data['errors']:
                messages.error(request, error)
            return redirect('wishlist:add_item')
    return redirect('wishlist:index')


def show(request, id):
    if request.method == "POST":
        this_item = Item.objects.get(id=id)
        context = {
            "item": this_item
        }
        return render(request, 'wishlist/show.html', context)


def add_wish(request):
    if request.method == "POST":
        item = Item.objects.get(id=request.POST['product_id'])
        user = User.objects.get(id=request.session['user_id'])
        item.users.add(user)
    return redirect('wishlist:index')

def delete(request):
    Item.objects.filter(id=request.POST['product_id']).delete()
    return redirect('wishlist:index')
