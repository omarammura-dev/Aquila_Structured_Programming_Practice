# Generated by Django 4.2.13 on 2024-05-23 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zoo_app', '0011_alter_visitor_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zoo_app.animal')),
                ('interaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zoo_app.interaction')),
                ('visitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zoo_app.visitor')),
            ],
        ),
    ]
