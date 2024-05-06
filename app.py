class ZooApp:
    def __init__(self, master):
        self.master = master
        self.master.title("My Zoo")
        self.zoo = Zoo()
        
        self.create_widgets()
        
    def create_widgets(self):
        self.info_label = tk.Label(self.master, text="Welcome to the Zoo !")
        self.info_label.pack()

        self.add_cage_button = tk.Button(self.master, text="Add habitat", command=self.add_cage)
        self.add_cage_button.pack()

        self.add_animal_button = tk.Button(self.master, text="Add Animal", command=self.add_animal)
        self.add_animal_button.pack()

        self.show_zoo_button = tk.Button(self.master, text="Show Zoo", command=self.show_zoo)
        self.show_zoo_button.pack()

    def add_cage(self):
        cage_name = tk.simpledialog.askstring("Cage Name", "Enter Cage Name:")
        if cage_name:
            cage = Cage()
            cage.name = cage_name
            self.zoo.add_cages([cage])

    def add_animal(self):
        animal_name = tk.simpledialog.askstring("Animal Name", "Enter Animal Name:")
        if animal_name:
            animal_type = tk.simpledialog.askstring("Animal Type", "Enter Animal Type:")
            if animal_type:
                animal = globals()[animal_type]()
                animal.name = animal_name
                self.zoo.cages[-1].add_animals([animal])

    def show_zoo(self):
        messagebox.showinfo("Zoo Information", str(self.zoo))


root = tk.Tk()
app = ZooApp(root)
root.mainloop()