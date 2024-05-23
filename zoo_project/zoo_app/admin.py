from django.contrib import admin
from .models import Habitat,Animal,Visitor

admin.site.register(Animal)
admin.site.register(Visitor)
admin.site.register(Habitat)