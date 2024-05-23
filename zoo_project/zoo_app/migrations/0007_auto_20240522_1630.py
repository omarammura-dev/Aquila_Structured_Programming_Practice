# Generated by Django 4.2.13 on 2024-05-20 15:20

from django.db import migrations

def create_animals(apps, schema_editor):
    Habitat = apps.get_model('zoo_app', 'Habitat')
    Animal = apps.get_model('zoo_app', 'Animal')

    # Assuming the habitats have already been created in previous migrations
    tropical_forest = Habitat.objects.get(name='Tropical Forest')
    arctic = Habitat.objects.get(name='Arctic')
    savannah = Habitat.objects.get(name='Savannah')

    # Add 10 new animals
    Animal.objects.create(name='Tiger', species='Mammal', age=7, breed='Bengal', health_status='Healthy', habitat=tropical_forest)
    Animal.objects.create(name='Elephant', species='Mammal', age=10, breed='African', health_status='Healthy', habitat=savannah)
    Animal.objects.create(name='Polar Bear', species='Mammal', age=8, breed='Arctic', health_status='Healthy', habitat=arctic)
    Animal.objects.create(name='Gorilla', species='Mammal', age=15, breed='Mountain', health_status='Healthy', habitat=tropical_forest)
    Animal.objects.create(name='Cheetah', species='Mammal', age=6, breed='African', health_status='Healthy', habitat=savannah)
    Animal.objects.create(name='Walrus', species='Mammal', age=10, breed='Arctic', health_status='Healthy', habitat=arctic)
    Animal.objects.create(name='Orangutan', species='Mammal', age=12, breed='Bornean', health_status='Healthy', habitat=tropical_forest)
    Animal.objects.create(name='Zebra', species='Mammal', age=7, breed='Plains', health_status='Healthy', habitat=savannah)
    Animal.objects.create(name='Seal', species='Mammal', age=9, breed='Harbor', health_status='Healthy', habitat=arctic)
    Animal.objects.create(name='Leopard', species='Mammal', age=8, breed='African', health_status='Healthy', habitat=savannah)

class Migration(migrations.Migration):

    dependencies = [
        ('zoo_app', '0006_animal_image'),
    ]

    operations = [
        migrations.RunPython(create_animals),
    ]