# Generated by Django 4.2.13 on 2024-05-22 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo_app', '0009_visitor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='age',
            field=models.IntegerField(blank=True),
        ),
    ]