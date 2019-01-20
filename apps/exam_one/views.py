from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from datetime import datetime
from ..app_one.models import *
from .models import Item
from django.contrib import messages

def main(request):
    # if 'user_id' not in request.session:
    #     return redirect('/')
    context = {
        # 'my_quote' : Quote.objects.filter(quote_created = request.session['user_id']),
        'user_name' : User.objects.get(id=request.session['user_id']),
        'items' : Item.objects.filter(item_add=request.session['user_id']),
        'this' : Item.objects.all(),
        'other': Item.objects.exclude(item_add=request.session['user_id'])
        # 'other_quote' : Quote.objects.exclude(quote_created = request.session['user_id'].all().values()),
        # 'allother_quote' : Quote.objects.exclude(quote_created = request.session['user_id']),
        # 'item' : Item.objects.all(),

    }
    return render(request,'exam_one/index.html', context)


def add(request):
    # user = User.objects.get(id=id)
    # item = Item.objects.get(id=id)
    # context = {
    #     'item' : item,
    # }

    return render(request,'exam_one/add.html')

def processadd(request):
    # item = Item.objects.get(id=id)
    if request.method=='POST':
        errors = Item.objects.item_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/exam/processadd')
        else:
            add_new_user = User.objects.get(id=request.session['user_id'])
            item = Item.objects.create(item = request.POST['item'],item_created = add_new_user)
            item.item_add.add(add_new_user)

    return redirect('/exam/')

def delete(request, number):
    item = Item.objects.get(id=number)
    user = User.objects.get(id=request.session['user_id'])
    item.delete()
    return redirect('/exam/')


def show(request, number):
    
    item = Item.objects.get(id=number)
    all_items = User.objects.filter(item_by_users=number)
    
    context = {
        'this_trip': item,
        'user1': all_items.exclude(id=item.item_created.id),
        'joined_trip': Item.objects.filter(id=request.session['user_id'])


    }
    return render(request, 'exam_one/destination.html', context)

