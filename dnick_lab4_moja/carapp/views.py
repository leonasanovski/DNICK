from django.shortcuts import render

from carapp.models import Car


# Create your views here.
def index(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request,'index.html',context)
def car_details(request, car_id):
    car = Car.objects.filter(id=car_id).first()
    context = {'car': car}
    return render(request,'details.html', context)