import random


class TimeManager:
    def __init__(self):
        self.daytime = "Day"

    def change_time(self):
        if random.random() < 0.5:
            self.daytime = "Night"
        else:
            self.daytime = "Day"