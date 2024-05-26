from animals import Animal, Predator, Bird, Herbivore
from visitors import Visitor
from cells import Cell
import cowsay

class Zoo:
    def __init__(self):
        self.cells = {}
        self.animals = []
        self.visitors = []
        self.default_animal_locations = {
            "Lion": "1",
            "Penguin": "2",
            "Tiger": "3",
            "Leopard": "4",
            "Elephant": "5"
        }
        self.default_animal_classes = {
            "Lion": Predator,
            "Penguin": Bird,
            "Tiger": Predator,
            "Leopard": Predator,
            "Elephant": Herbivore
        }
        self.initialize_animals()

    def initialize_animals(self):
        for animal_name, cell_number in self.default_animal_locations.items():
            if cell_number not in self.cells:
                self.cells[cell_number] = Cell(cell_number)
            animal_class = self.default_animal_classes[animal_name]
            animal = animal_class(animal_name, "adult", "good", "Africa", "male")
            self.cells[cell_number].add_animal(animal)
            self.animals.append(animal)

    def add_cell(self, cell_number):
        if cell_number not in self.cells:
            self.cells[cell_number] = Cell(cell_number)
            print(f"Cell number {cell_number} successfully added for animals.")
        else:
            print("This cell number already exists.")

    def add_animal_to_cell(self, cell_number, animal):
        if animal in self.animals:
            print("This animal is already in the zoo.")
        else:
            if cell_number in self.cells:
                self.cells[cell_number].add_animal(animal)
                self.animals.append(animal)  
                print(f"Animal {animal.name} successfully added to the cell.")
            else:
                print("Cell not found.")

    def remove_animal_from_cell(self, cell_number, animal_name):
        if cell_number in self.cells:
            self.cells[cell_number].remove_animal(animal_name)
            print("Animal removed from the cell.")
        else:
            print("Cell not found.")

    def remove_cell(self, cell_number):
        if cell_number in self.cells:
            del self.cells[cell_number]
            print("Cell deleted.")
        else:
            print("Cell not found.")

    def add_visitor(self):
        print("Choose visitor status:")
        print("1. Alone")
        print("2. Student")
        print("3. Teacher")
        print("4. Family")
        print("5. Friends")
        visitor_type_choice = input("Your choice: ")
        
        if visitor_type_choice == '1':
            name = input("Enter name: ")
            age = input("Enter age: ")
            preferences = input("Enter preferences: ")
            self.visitors.append(Visitor(name, age, "Alone" , preferences))
            print("Visitor added.")
        elif visitor_type_choice == '2':
            name = input("Enter name: ")
            age = input("Enter age: ")
            preferences = input("Enter preferences: ")
            self.visitors.append(Visitor(name, age, "Student",preferences))
            print("Visitor added.")
        elif visitor_type_choice == '3':
            name = input("Enter name: ")
            age = input("Enter age: ")
            preferences = input("Enter preferences: ")
            self.visitors.append(Visitor(name, age, "Teacher",preferences))
            print("Visitor added.")
        elif visitor_type_choice == '4':
            num_people = int(input("Enter the number of people who came together: "))
            for i in range(num_people):
                name = input(f"Enter name of person {i+1}: ")
                age = input(f"Enter age of person {i+1}: ")
                preferences = input(f"Enter preferences of person {i+1}: ")
                self.visitors.append(Visitor(name, age, "Family",preferences))
            print("Visitors added.")
        elif visitor_type_choice == '5':
            num_people = int(input("Enter the number of friends who came together: "))
            for i in range(num_people):
                name = input(f"Enter name of friend {i+1}: ")
                age = input(f"Enter age of friend {i+1}: ")
                preferences = input(f"Enter preferences of friend {i+1}: ")
                self.visitors.append(Visitor(name, age, "Friends",preferences))
            print("Visitors added.")
        else:
            print("Invalid choice.")

    def remove_visitor(self, visitor_name):
        self.visitors = [v for v in self.visitors if v.name != visitor_name]
        print("Visitor removed.")

    def list_animals_in_cell(self, cell_number):
        if cell_number in self.cells:
            animals = self.cells[cell_number].animals
            if animals:
                print(f"Animals in cell number {cell_number}:")
                for animal in animals:
                    print(f"Name: {animal.name}, Species: {animal.species}, Class: {type(animal).__name__}, Age: {animal.age}, Gender: {animal.gender}, Health: {animal.health}, Region: {animal.region}")
            else:
                print("There are no animals in this cell.")
        else:
            print("Cell not found.")

    def list_all_cells(self):
        return list(self.cells.keys())

    def list_all_animals_in_zoo(self):
        return [animal.name for animal in self.animals]

    def interact_with_animal(self, animal_name):
        print(f"Interacting with {animal_name}...")

    def observe_animals(self):
        print("Observing animals...")

    def play_with_animals(self):
        print("Playing with animals...")

    def feed_animals(self):
        print("Feeding animals...")

    def update_animal_info(self, animal_name):
        found = False
        for animal in self.animals:
            if animal.name == animal_name:
                found = True
                print("Updating information about animal:", animal_name)
                new_age = input("Enter new age: ")
                new_health = input("Enter new health status (good or bad): ")
                animal.age = new_age
                animal.health = new_health
                print("Information about animal successfully updated.")
                break
        if not found:
            print("Animal with name", animal_name, "not found in the zoo.")

    def show_all_visitors(self):
        print("List of visitors:")
        for visitor in self.visitors:
            print(f"Name: {visitor.name}, Age: {visitor.age}, Type: {visitor.visitor_type}, Preferences: {visitor.animal_list}")

def main_menu(zoo):
    while True:
        cowsay.cow("WELCOME TO THE ZOO")
        print("\nChoose an action:\n")
        print("1. Add a cell                        6. Remove an animal from a cell")
        print("2. Add an animal to a cell           7. Remove a cell")
        print("3. Add a visitor                     8. Remove a visitor")
        print("4. List animals in a cell            9. List all animals in the zoo")
        print("5. List all cells                    10. Interact with an animal")
        print("11. Exit the zoo                      12. Update animal information")
        print("13. Show list of visitors\n")
        
        choice = input("Your choice: ")

        if choice == '1':
            cell_number = input("Enter cell number: ")
            zoo.add_cell(cell_number)

        elif choice == '2':
            cell_number = input("Enter cell number: ")
            animal_name = input("Enter animal name: ")
            animal_species = input("Enter animal species: ")
            animal_age = input("Enter animal age: ")
            animal_health = input("Enter animal health status (good or bad): ")
            animal_region = input("Enter region: ")
            animal_gender = input("Enter animal gender (m/f): ")
            animal = Animal(animal_name, animal_species, animal_age, animal_health, animal_region, animal_gender)
            zoo.add_animal_to_cell(cell_number, animal)

        elif choice == '3':
            zoo.add_visitor()

        elif choice == '4':
            cell_number = input("Enter cell number: ")
            zoo.list_animals_in_cell(cell_number)

        elif choice == '5':
            cells = zoo.list_all_cells()
            print("All cells:", cells)

        elif choice == '6':
            cell_number = input("Enter cell number: ")
            animal_name = input("Enter animal name to remove: ")
            zoo.remove_animal_from_cell(cell_number, animal_name)

        elif choice == '7':
            cell_number = input("Enter cell number to remove: ")
            zoo.remove_cell(cell_number)

        elif choice == '8':
            visitor_name = input("Enter visitor name to remove: ")
            zoo.remove_visitor(visitor_name)

        elif choice == '9':
            all_animals = zoo.list_all_animals_in_zoo()
            print("All animals in the zoo:", all_animals)

        elif choice == '10':
            all_animals = zoo.list_all_animals_in_zoo()
            print("All animals in the zoo:")
            for idx, animal in enumerate(all_animals, start=1):
                print(f"{idx}. {animal}")
            choice_index = int(input("Choose animal number to interact with: ")) - 1
            chosen_animal = all_animals[choice_index]
            zoo.interact_with_animal(chosen_animal)

            all_visitors = zoo.visitors
            print("All visitors:")
            for idx, visitor in enumerate(all_visitors, start=1):
                print(f"{idx}. {visitor.name}")

            choice_visitor_index = int(input("Choose visitor number to interact with: ")) - 1
            chosen_visitor = all_visitors[choice_visitor_index]
            print(f"Interaction {chosen_visitor.name} with animal {chosen_animal}...")

            print("Choose action:")
            print("1. Feed the animal")
            print("2. Play with the animal")
            print("3. Observe the animal")
            interaction_choice = input("Your choice: ")
            if interaction_choice == '1':
                zoo.feed_animals()
            elif interaction_choice == '2':
                zoo.play_with_animals()
            elif interaction_choice == '3':
                zoo.observe_animals()
            else:
                print("Invalid input. Please try again.")

        elif choice == '11':
            print("Exiting the zoo.")
            break

        elif choice == '12':
            animal_name = input("Enter animal name to update: ")
            zoo.update_animal_info(animal_name)

        elif choice == '13':
            if not zoo.visitors:
                print("List of visitors is empty.")
            else:
                zoo.show_all_visitors()

        else:
            print("Invalid input. Please try again.")

        input("\nPress Enter to continue...")

def main():
    zoo = Zoo()
    while True:
        main_menu(zoo)
        repeat = input("Press any key to open the menu again or enter 'exit' to quit: ")
        if repeat.lower() == 'exit':
            break

if __name__ == "__main__":
    main()
