from django.db import models

class Habitat(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(blank=True)

class Animal(models.Model):
    SPECIES_CHOICES = [
    ('Lion', 'Lion'),
    ('Tiger', 'Tiger'),
    ('Elephant', 'Elephant'),
    ('Polar Bear', 'Polar Bear'),
    ('Gorilla', 'Gorilla'),
    ('Cheetah', 'Cheetah'),
    ('Walrus', 'Walrus'),
    ('Orangutan', 'Orangutan'),
    ('Zebra', 'Zebra'),
    ('Seal', 'Seal'),
    ('Leopard', 'Leopard'),
    ('Penguin', 'Penguin'),
    ]

    HEALTH_STATUS_CHOICES = [
        ('Healthy', 'Healthy'),
        ('Sick', 'Sick'),
    ]

    name = models.CharField(max_length=200, default="I don't have a name dude!")
    species = models.CharField(max_length=200, choices=SPECIES_CHOICES)
    age = models.IntegerField()
    breed = models.CharField(max_length=200)
    health_status = models.CharField(max_length=200, choices=HEALTH_STATUS_CHOICES)
    habitat = models.ForeignKey(Habitat, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)
    def eat(self):
        print(f"{self.name} ate")

    def sleep(self):
        print(f"{self.name} slept")

    def move(self):
        print(f"{self.name} moved")

class Visitor(models.Model):
    habitats = [
        ('Savannah','Savannah'),
        ('Arctic','Arctic'),
        ('Tropical Forest','Tropical Forest')
    ]
    age = models.IntegerField(blank=True,null=True)
    group_type = models.CharField(max_length=200)
    habitat = models.ForeignKey(Habitat,on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, null=True) 



class Interaction(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def perform_interaction(self, animal, visitor):
        print(f"the visitor {visitor} is interacting with {animal} the event is : {self.name}")
        

class Event(models.Model):
    interaction = models.ForeignKey(Interaction, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)

    def trigger_event(self):
        self.interaction.perform_interaction(self.animal, self.visitor)