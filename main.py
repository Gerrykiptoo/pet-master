#!/usr/bin/env python3
#!/usr/bin/env python3
#!/usr/bin/env python3
#!/usr/bin/env python3

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    def sleep(self):
        self.energy = min(10, self.energy + 5)

    def get_status(self):
        status = f"""
        {'='*25}
        {self.name}'s Status:
        {'-'*25}
        Hunger:    {'⭐' * self.hunger}{'◻' * (10 - self.hunger)}
        Energy:    {'⚡' * self.energy}{'◻' * (10 - self.energy)}
        Happiness: {'❤' * self.happiness}{'◻' * (10 - self.happiness)}
        {'='*25}
        """
        print(status)

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        print(f"✨ {self.name} learned {trick}!")

    def show_tricks(self):
        if not self.tricks:
            print(f"\n{self.name} hasn't learned any tricks yet!")
            return
        print(f"\n{self.name}'s tricks:")
        print("-"*20)
        for i, trick in enumerate(self.tricks, 1):
            print(f"{i}. {trick}")
                
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    def sleep(self):
        self.energy = min(10, self.energy + 5)

    def get_status(self):
        status = f"""
        {'='*25}
        {self.name}'s Status:
        {'-'*25}
        Hunger:    {'⭐' * self.hunger}{'◻' * (10 - self.hunger)}
        Energy:    {'⚡' * self.energy}{'◻' * (10 - self.energy)}
        Happiness: {'❤' * self.happiness}{'◻' * (10 - self.happiness)}
        {'='*25}
        """
        print(status)

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        print(f"✨ {self.name} learned {trick}!")

    def show_tricks(self):
        if not self.tricks:
            print(f"\n{self.name} hasn't learned any tricks yet!")
            return
        print(f"\n{self.name}'s tricks:")
        print("-"*20)
        for i, trick in enumerate(self.tricks, 1):
            print(f"{i}. {trick}")                                                                                                 