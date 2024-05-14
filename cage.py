
class Cage:
    """ Contains a list of animals inside and performs methods to check
    intern competition where there might be a conflict of prey and predator,
    where a prey gets eaten.
    """

    def __init__(self):
        self.animals_list = []
        self.name = 'Cage'      # Default name configuration

    def __repr__(self):
        if len(self.animals_list) > 0:      # Checks if cage isn't empty
            return "{} contains {} animal(s): {}".format(
                self.name, self.n_of_animals(),
                ', '.join(map(str, self.animals_list)))
        else:
            return "{} (empty)".format(self.name)

    def n_of_animals(self):
        return len(self.animals_list)

    def check_prey(self):
        """ Method for checking the animals chain food competition inside a
        cage: iterates through its animals list and kills (deletes) the
        predator's prey.
        """
        death_statements = {}       # Dictionary to handle preys getting eaten
        # Check if any animals in the list have listed prey inside this cage:
        for predator in self.animals_list:
            for prey in self.animals_list:      # Parses animals prey's lists
                """ Compares the listed classes in an animal's prey list
                with the class of each other animal on the cage. """
                if type(prey) in predator.prey:
                    death_statements[prey] = (prey, "{} got eaten by {}."
                                              .format(prey, predator))
        if len(death_statements) > 0:       # Checks if there were any deaths
            print("Oops! Seems like you put predator and prey on same cage.")
            for prey in death_statements:
                print(death_statements[prey][1])        # Prints name of prey
                self.animals_list.remove(death_statements[prey][0])
                # Prints statement of death identifying the predator
        print('Now ' + str(self))       # Shows updated list of animals in cage

    def add_animals(self, add_list):
        """ Inserts animals inside the Cage object. """
        duplicate_animals = []
        for animal in add_list:
            """ Checks if the parent class of the list item is not an Animal
            object (in this case, the item won't be inserted in the Cage)
            """
            if animal.__class__.__base__ != Animal:
                print("{} object could not be added because it's not an "
                      "Animal subclass.".format(animal.__class__.__name__))
            elif animal not in self.animals_list:
                self.animals_list.append(animal)
                # Inserts Animal object in cage if not already inside
            elif animal not in duplicate_animals:
                    duplicate_animals.append(animal)
        if len(duplicate_animals) > 0:      # Checks duplicate insert attempt
            print("Duplicate animal(s) found: {} already inside.".format(
                ', '.join(map(str, duplicate_animals))))
            print(self)
        return self.check_prey()
        # Starts check on whether there is prey and predator on the same cage
