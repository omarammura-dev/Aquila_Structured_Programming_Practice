class Animal:
    def __init__(self, name, species, age, health, region, gender):
        self.name = name
        self.species = species
        self.age = age
        self.health = health
        self.region = region
        self.gender = gender

class Predator(Animal):
    def __init__(self, name, age, health, region, gender):
        super().__init__(name, "vahşi", age, health, region, gender)

class Bird(Animal):
    def __init__(self, name, age, health, region, gender):
        super().__init__(name, "Kuş", age, health, region, gender)

class Herbivore(Animal):
    def __init__(self, name, age, health, region, gender):
        super().__init__(name, "Otobur", age, health, region, gender)
