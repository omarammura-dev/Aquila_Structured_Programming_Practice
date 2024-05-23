# Generated by Django 4.2.13 on 2024-05-20 15:09

from django.db import migrations, models
import django.db.models.deletion

def create_habitats(apps, schema_editor):
    Habitat = apps.get_model('zoo_app', 'Habitat')
    Animal = apps.get_model('zoo_app', 'Animal')

    tropical_forest = Habitat.objects.create(name='Tropical Forest',image_url="../static/zoo_app/forest.jpeg")
    arctic = Habitat.objects.create(name='Arctic',image_url="../static/zoo_app/polar.jpeg")
    savannah = Habitat.objects.create(name='Savannah',image_url="../static/zoo_app/savannah.webp")

    Animal.objects.create(name='Penguin', species='Bird', age=5, breed='Emperor', health_status='Healthy', habitat=arctic)
    Animal.objects.create(name='Lion', species='Mammal', age=8, breed='African Lion', health_status='Healthy', habitat=savannah)

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('image_url', models.CharField(default='default_image_url', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default="I don't have a name dude!", max_length=200)),
                ('species', models.CharField(choices=[('Lion', 'Lion'), ('Tiger', 'Tiger')], max_length=200)),
                ('age', models.IntegerField()),
                ('breed', models.CharField(max_length=200)),
                ('health_status', models.CharField(choices=[('Healthy', 'Healthy'), ('Sick', 'Sick')], max_length=200)),
                ('habitat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zoo_app.habitat')),
            ],
        ),
    ]