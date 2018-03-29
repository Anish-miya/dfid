from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .models import Provinces
from django.views.generic.edit import UpdateView
from django.urls import resolve
from .forms import ProvinceForm



def index(request):
    provinces = Provinces.objects.all()
    context = {'provinces': provinces}
    return render(request, 'main/index.html', context)


def create(request):
    print(request.POST)
    province = Provinces(province_name=request.POST['province_name'], minister_name=request.POST['minister_name'], capital=request.POST['capital'], districts=request.POST['districts'])
    province.save()
    return redirect('/')


def destroy(request, id):
    province = Provinces.objects.get(id=id)
    province.delete()
    return redirect('/')


def update(request):
    provinces = Provinces.objects.all()
    context = {'provinces': provinces}
    return render(request, 'main/edit.html', context)










