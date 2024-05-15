import tkinter as tk
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
        self.master.configure(background="#FFF9D0")

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
        self.clock_label = tk.Label(master, text="", background="#FFF9D0", font=("Arial", 14))
        self.clock_label.pack(anchor="ne", padx=20, pady=10)
        self.update_clock()

        # Search bar
        self.search_label = tk.Label(master, text="Search:", font=("Arial", 10), background="#FFF9D0")
        self.search_label.pack(padx=20, pady=(10, 0), anchor="w")
        self.search_entry = tk.Entry(master, font=("Arial", 10))
        self.search_entry.pack(padx=20, pady=(0, 10), ipady=3, fill=tk.X)

        # Frame to hold all habitats
        self.habitat_frame = tk.Frame(master, background="#FFF9D0")
        self.habitat_frame.pack(fill="both", expand=True)

        for i, (habitat_name, habitat) in enumerate(self.habitats.items()):
            habitat_frame = tk.Frame(self.habitat_frame, background="#FFF9D0")
            habitat_frame.grid(row=0, column=i, sticky="nsew")
            self.habitat_frame.grid_columnconfigure(i, weight=1)  # Center the habitat frames

            habitat_label = tk.Label(habitat_frame, text=habitat_name, font=("Arial", 14, "bold"), background="#FFF9D0")
            habitat_label.pack(pady=(10, 0))

            image_path = os.path.join(self.image_folder, f"{habitat_name.lower().replace(' ', '_')}.jpg")
            image = Image.open(image_path)
            image = image.resize((200, 200), Image.BILINEAR)
            photo = ImageTk.PhotoImage(image)

            label = tk.Label(habitat_frame, image=photo, background="#FFF9D0", borderwidth=1, relief="solid")
            label.image = photo  # Keep a reference to the image
            label.pack(expand=True, padx=20, pady=10)
            label.bind("<Button-1>", lambda event, h=habitat_name: self.add_animal_window(h))

        # Add button at the bottom center
        self.add_visitor_button = tk.Button(master, text="Add", command=self.open_dashboard_window, font=("Arial", 10), bg="#CAF4FF", bd=0, highlightthickness=0, padx=10, pady=5, relief=tk.FLAT)
        self.add_visitor_button.place(relx=0.5, rely=1.0, anchor=tk.S)

    def add_animal_window(self, habitat_name):
        window = tk.Toplevel(self.master)
        window.title(f"Add Animal to {habitat_name}")
        add_animal_button = tk.Button(window, text="Add Animal", command=lambda h=habitat_name: self.add_animal(h))
        add_animal_button.pack(pady=10, padx=20, ipady=3, fill=tk.X)

    def add_animal(self, habitat_name):
        pass

    def open_dashboard_window(self):
        if self.dashboard_window is None or not tk.Toplevel.winfo_exists(self.dashboard_window):
            self.dashboard_window = tk.Toplevel(self.master)
            self.dashboard_window.title("Day and Visitor Count")
            day_label = tk.Label(self.dashboard_window, text=f"Day: {self.day}", font=("Arial", 14), background="#FFF9D0")
            day_label.pack(pady=(20, 5))
            visitor_count_label = tk.Label(self.dashboard_window, text=f"Visitor count: {len(self.visitors)}", font=("Arial", 14), background="#FFF9D0")
            visitor_count_label.pack(pady=5)
            add_visitor_button = tk.Button(self.dashboard_window, text="Add Visitor", command=self.add_random_visitors, font=("Arial", 10), bg="#CAF4FF", bd=0, highlightthickness=0, padx=10, pady=5, relief=tk.FLAT)
            add_visitor_button.pack(pady=(5, 20))

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
            day_label = tk.Label(self.dashboard_window, text=f"Day: {self.day}", font=("Arial", 14), background="#FFF9D0")
            day_label.pack(pady=(20, 5))
            visitor_count_label = tk.Label(self.dashboard_window, text=f"Visitor count: {len(self.visitors)}", font=("Arial", 14), background="#FFF9D0")
            visitor_count_label.pack(pady=5)
            add_visitor_button = tk.Button(self.dashboard_window, text="Add Visitor", command=self.add_random_visitors, font=("Arial", 10), bg="#CAF4FF", bd=0, highlightthickness=0, padx=10, pady=5, relief=tk.FLAT)
            add_visitor_button.pack(pady=(5, 20))

    def update_clock(self):
        now = datetime.now()
        if not hasattr(self, "current_time"):
            random_hour = random.randint(0, 23)
            random_minute = random.randint(0, 59)
            random_second = random.randint(0, 59)
            self.current_time = now.replace(hour=random_hour, minute=random_minute, second=random_second)

        if self.current_time.time() > time(6, 0) and self.current_time.time() < time(18, 0):
            self.clock_label.config(text=f"Day Time: {self.current_time.strftime('%H:%M:%S')}")
        else:
            self.clock_label.config(text=f"Night Time: {self.current_time.strftime('%H:%M:%S')}")

        self.current_time += timedelta(seconds=1)
        self.master.after(1000, self.update_clock)


root = tk.Tk()
app = ZooApp(root)
root.mainloop()


