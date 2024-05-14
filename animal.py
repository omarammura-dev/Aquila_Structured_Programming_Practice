class Animal:
    def __init__(self, species, age, breed, health_status):
        self.species = species
        self.age = age
        self.breed = breed
        self.health_status = health_status
        self.name = 'I don\'t have a name dude!'     

    def eat(self):
        pass

    def sleep(self):
        pass

    def move(self):
        pass

class Animal:
    def __init__(self, species, age, breed, health_status):
        self.species = species
        self.age = age
        self.breed = breed
        self.health_status = health_status
        self.name = 'I don\'t have a name dude!'     

    def eat(self):
        pass

    def sleep(self):
        pass

    def move(self):
        pass    


class Lion(Animal):
    def __init__(self, species, age, breed, health_status):
        super().__init__(species, age, breed, health_status)
        self.name = 'Lion'

    def hunt(self):
        print("The lion is hunting")

class Elephant(Animal):
    def __init__(self, species, age, breed, health_status):
        super().__init__(species, age, breed, health_status)
        self.name = 'Elephant'

class Penguin(Animal):
    def __init__(self, species, age, breed, health_status):
        super().__init__(species, age, breed, health_status)
        self.name = 'Penguin'

    def swim(self):
        print("The penguin is swimming")    