class Visitor:
    def __init__(self, name, age, visitor_type, animal_list=None):
        self.name = name
        self.age = age
        self.visitor_type = visitor_type
        self.animal_list = animal_list if animal_list is not None else []
