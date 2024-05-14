import tkinter as tk
from tkinter import ttk
import random
from visitor import Visitor
from habitat import Habitat

class ZooApp:
    def __init__(self, master):
        self.master = master
        self.master.title("ZooApp Dashboard")
        self.master.geometry("800x600")

        self.animals = []  
        self.visitors = []
        self.day = 0

        self.habitats = {
            'Savannah': Habitat('Savannah'),
            'Polar Region': Habitat('Polar Region'),
            'Tropical Forest': Habitat('Tropical Forest')
        }

        self.tree = ttk.Treeview(master)
        self.tree.pack()

        for habitat_name, habitat in self.habitats.items():
            self.tree.insert("", "end", text=habitat_name)

        self.tree.bind("<Double-1>", self.on_habitat_click)

        self.add_visitor_button = tk.Button(master, text="Add Visitor", command=self.add_random_visitors)
        self.add_visitor_button.pack()

        self.day_label = tk.Label(master, text=f'Day: {self.day}')
        self.day_label.pack()

    def on_habitat_click(self, event):
        item_id = self.tree.focus()
        habitat_name = self.tree.item(item_id, "text")
        window = tk.Toplevel(self.master)
        window.title(habitat_name)
        for cage in self.habitats[habitat_name].cages:
            label = tk.Label(window, text=str(cage))
            label.pack()

        button = tk.Button(window, text="Add Animal", command=self.add_animal)
        button.pack()

    def add_animal(self):
        pass

    def add_random_visitors(self):
        for _ in range(random.randint(1, 10)):
            age = random.randint(1, 100)
            group_type = random.choice(['Family', 'School', 'Individual'])
            visitor = Visitor(age, group_type)
            self.visitors.append(visitor)
        self.update_dashboard()

    def update_dashboard(self):
        self.day += 1
        self.day_label.config(text=f'Day: {self.day}')
        visitor_count_label = tk.Label(self.master, text=f'Visitor count: {len(self.visitors)}')
        visitor_count_label.pack()
root = tk.Tk()
app = ZooApp(root)
root.mainloop()