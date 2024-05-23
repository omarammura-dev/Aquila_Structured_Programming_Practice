from django.shortcuts import render,redirect
from .models import Habitat, Animal,Visitor,Interaction,Event
from django.http import JsonResponse
import random

def dashboard(request, habitat_id=None):
    day = 1
    visitors = 10
    habitats = Habitat.objects.all()  
    context = {'day': day, 'visitors': visitors, 'habitats': habitats}
    return render(request, 'dashboard.html', context)

def list_animals(request, habitat_id):
    habitat = Habitat.objects.get(id=habitat_id)
    animals = Animal.objects.filter(habitat=habitat)
    visitors = Visitor.objects.filter(habitat=habitat)
    context = {'habitat': habitat, 'animals': animals, 'visitors': visitors}
    return render(request, 'list_animals.html', context)

def add_random_visitors(request,habitat_id):
    visitors = []
    habitat = Habitat.objects.get(id=habitat_id)
    animals = Animal.objects.filter(habitat=habitat)
    group_type = random.choice(['Family', 'School', 'Individual'])
    if group_type == 'Individual':
        age = random.randint(18, 100)
    else:
        age = None
    visitor = Visitor.objects.create(age=age, group_type=group_type, habitat=habitat)
    visitors.append(visitor)  
    return redirect('list_animals', habitat_id=habitat_id)

def add_animal(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        habitat_id = request.POST.get('age')
        habitat = Habitat.objects.get(id=habitat_id)
        Animal.objects.create(name=name, habitat=habitat)
    return redirect('dashboard')


def animal_eat(request, id):
    animal = Animal.objects.get(pk=id)
    interaction = Interaction.objects.create(name='eat')
    visitor = Visitor.objects.filter(habitat=animal.habitat).first()
    event = Event.objects.create(interaction=interaction, animal=animal, visitor=visitor)
    animal.eat()
    event.trigger_event()
    return JsonResponse({'status': 'success'})

def animal_move(request, id):
    animal = Animal.objects.get(pk=id)
    interaction = Interaction.objects.create(name='move')
    visitor = Visitor.objects.filter(habitat=animal.habitat).first()
    event = Event.objects.create(interaction=interaction, animal=animal, visitor=visitor)
    animal.eat()
    event.trigger_event()
    return JsonResponse({'status': 'success'})

def animal_sleep(request, id):
    animal = Animal.objects.get(pk=id)
    interaction = Interaction.objects.create(name='sleep')
    visitor = Visitor.objects.filter(habitat=animal.habitat).first()
    animal.sleep()
    event = Event.objects.create(interaction=interaction, animal=animal, visitor=visitor)
    event.trigger_event()
    return JsonResponse({'status': 'success'})

def animal_birth(request, id):
    animal = Animal.objects.get(pk=id)
    interaction = Interaction.objects.create(name='birth')
    visitor = Visitor.objects.filter(habitat=animal.habitat).first()
    event = Event.objects.create(interaction=interaction, animal=animal, visitor=visitor)
    event.trigger_event()
    return JsonResponse({'status': 'success'})

def animal_hunt(request, id):
    animal = Animal.objects.get(pk=id)
    interaction = Interaction.objects.create(name='hunt')
    visitor = Visitor.objects.filter(habitat=animal.habitat).first()
    event = Event.objects.create(interaction=interaction, animal=animal, visitor=visitor)
    event.trigger_event()
    return JsonResponse({'status': 'success'})