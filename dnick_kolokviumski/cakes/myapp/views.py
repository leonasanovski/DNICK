import random

from django.shortcuts import render, redirect

from myapp.forms import AddCakeForm
from myapp.models import Cake, Baker


# Create your views here.
def index(request):
    products = Cake.objects.all()
    return render(request,'index.html',context={'products':products})
def add_cake(request):
    if request.method == 'POST':
        form = AddCakeForm(request.POST, request.FILES)
        if form.is_valid():
            baker = random.choice(Baker.objects.all())
            cake = form.save(commit=False)
            cake.baker = baker
            cake.save()
        return redirect("index")
    add_cake_form = AddCakeForm()
    context = {'form':add_cake_form}
    return render(request, 'add.html', context)