from django.shortcuts import render
from .models import Animals

def index (request):
    animals=Animals.objects.all()
    return render(request,'animals.html',{'animals': animals})


def single_animal (request,animal_id):
    animal=Animals.objects.get(pk=animal_id)
    return render(request,'single_animal.html',{'animal': animal})




# Create your views here.
