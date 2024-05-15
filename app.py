import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import random
from visitor import Visitor
from habitat import Habitat
from datetime import datetime, time, timedelta

class ZooApp:
    def __init__(self, master):
        self.master = master
        self.master.title("ZooApp Dashboard")
        self.master.geometry("800x600")
        self.master.configure(bg='lightblue')  # Изменение цвета фона

        self.animals = []  
        self.visitors = []
        self.day = 0
        self.dashboard_window = None

        self.habitats = {
            'Savannah': Habitat('Savannah'),
            'Polar Region': Habitat('Polar Region'),
            'Tropical Forest': Habitat('Tropical Forest')
        }

        self.image_folder = os.path.dirname(os.path.abspath(__file__))  # Get the path of the image folder

        # Clock Widget
        self.clock_label = tk.Label(master, text="", font=("Helvetica", 18), fg='darkblue', bg='lightblue')
        self.clock_label.pack(anchor="ne", padx=10, pady=10)
        self.update_clock()

        # Search bar
        self.search_label = tk.Label(master, text="Search for animal:", font=("Helvetica", 16), fg='darkblue', bg='lightblue')
        self.search_label.pack(padx=10, pady=10)
        self.search_entry = tk.Entry(master)
        self.search_entry.pack(padx=10, pady=10)

        # Frame to hold all habitats
        self.habitat_frame = tk.Frame(master)
        self.habitat_frame.pack(fill="both", expand=True, padx=10, pady=10)

        for i, (habitat_name, habitat) in enumerate(self.habitats.items()):
            frame = tk.Frame(self.habitat_frame, borderwidth=2, relief="groove")
            frame.grid(row=0, column=i, sticky="nsew", padx=10, pady=10)
            
            self.habitat_frame.grid_columnconfigure(i, weight=1)  # Center the habitat frames

            habitat_label = tk.Label(frame, text=habitat_name, font=("Arial", 20, "bold"))
            habitat_label.pack(padx=10, pady=10)

            image_path = os.path.join(self.image_folder, f"{habitat_name.lower().replace(' ', '_')}.jpg")
            image = Image.open(image_path)
            image = image.resize((200, 200), Image.BILINEAR)
            photo = ImageTk.PhotoImage(image)

            label = tk.Label(frame, image=photo)
            label.image = photo  # Keep a reference to the image
            label.pack(expand=True, fill="both")

            frame.grid_propagate(False)  # Prevent frame from resizing to fit its contents

            # Bind the function to both the habitat label and the image label
            habitat_label.bind("<Button-1>", lambda event, h=habitat_name: self.add_animal_window(h))
            label.bind("<Button-1>", lambda event, h=habitat_name: self.add_animal_window(h))

        self.add_visitor_button = tk.Button(master, text="Add Visitor", command=self.open_dashboard_window, font=("Arial", 16))
        self.add_visitor_button.pack(padx=10, pady=10)

    def add_animal_window(self, habitat_name):
        window = tk.Toplevel(self.master)
        window.title(f"Add Animal to {habitat_name}")
        add_animal_button = tk.Button(window, text="Add Animal", command=lambda h=habitat_name: self.add_animal(h))
        add_animal_button.pack(padx=10, pady=10)

    def add_animal(self, habitat_name):
        pass

    def open_dashboard_window(self):
        if self.dashboard_window is None or not tk.Toplevel.winfo_exists(self.dashboard_window):
            self.dashboard_window = tk.Toplevel(self.master)
            self.dashboard_window.title("Day and Visitor Count")
            day_label = tk.Label(self.dashboard_window, text=f"Day: {self.day}", font=("Arial", 16))
            day_label.pack(padx=10, pady=10)
            visitor_count_label = tk.Label(self.dashboard_window, text=f"Visitor count: {len(self.visitors)}", font=("Arial", 16))
            visitor_count_label.pack(padx=10, pady=10)
            add_visitor_button = tk.Button(self.dashboard_window, text="Add Visitor", command=self.add_random_visitors, font=("Arial", 16))
            add_visitor_button.pack(padx=10, pady=10)

    def add_random_visitors(self):
        for _ in range(random.randint(1, 10)):
            age = random.randint(1, 100)
            group_type = random.choice(['Family', 'School', 'Individual'])
            visitor = Visitor(age, group_type)
            self.visitors.append(visitor)
        self.update_dashboard()

    def update_dashboard(self):
        self.day += 1
        if self.dashboard_window is not None and tk.Toplevel.winfo_exists(self.dashboard_window):
            for widget in self.dashboard_window.winfo_children():
                widget.destroy()
            day_label = tk.Label(self.dashboard_window, text=f"Day: {self.day}", font=("Arial", 16))
            day_label.pack(padx=10, pady=10)
            visitor_count_label = tk.Label(self.dashboard_window, text=f"Visitor count: {len(self.visitors)}", font=("Arial", 16))
            visitor_count_label.pack(padx=10, pady=10)
            add_visitor_button = tk.Button(self.dashboard_window, text="Add Visitor", command=self.add_random_visitors, font=("Arial", 16))
            add_visitor_button.pack(padx=10, pady=10)

    def update_clock(self):
        now = datetime.now()
        if not hasattr(self, "current_time"):
            random_hour = random.randint(0, 23)
            random_minute = random.randint(0, 59)
            random_second = random.randint(0, 59)
            self.current_time = now.replace(hour=random_hour, minute=random_minute, second=random_second)

        if self.current_time.time() > time(6, 0) and self.current_time.time() < time(18, 0):
            self.clock_label.config(text=f"Day Time: {self.current_time.strftime('%H:%M:%S')}", font=("Arial", 16))
        else:
            self.clock_label.config(text=f"Night Time: {self.current_time.strftime('%H:%M:%S')}", font=("Arial", 16))

        self.current_time += timedelta(seconds=1)
        self.master.after(1000, self.update_clock)


root = tk.Tk()
app = ZooApp(root)
root.mainloop()


