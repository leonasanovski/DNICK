from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from myapp.forms import AddRealEstate
from myapp.models import RealEstate, CharacteristicRealEstate


# Create your views here.
# Web апликацијата се состои од една почетна страна,
# прикажана на сликата подолу која ги прикажува сите недвижности кои не се продадени и нивната површина е поголема од 100 метри квадратни.

def index(request):
    dictionary = {}
    real_estates_to_show = RealEstate.objects.filter(Q(surface__gt=100) & Q(isSold=False)).all()
    for real_estate in real_estates_to_show:
        characteristics = CharacteristicRealEstate.objects.filter(real_estate=real_estate).all()
        total_price = sum(obj.characteristic.price or 0 for obj in characteristics)
        dictionary[real_estate] = total_price
    print(dictionary)
    return render(request, 'index.html', {'dict': dictionary})


def add_real_estate(request):
    if request.method == 'POST':
        form = AddRealEstate(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = AddRealEstate()
    return render(request, 'add_real_estate.html', context={'form': form})


def edit_real_estate(request, real_estate_id):
    real_estate = get_object_or_404(RealEstate, pk=real_estate_id)
    if request.method == 'POST':
        form = AddRealEstate(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = AddRealEstate(instance=real_estate)
    return render(request, 'edit_real_estate.html', context={'form': form, 'real_estate_id': real_estate_id, 'real_estate': real_estate})
