class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def make_sound(self):
        print(f"{self.name} makes a sound.")

    def to_dict(self):
        return {"type": "Animal", "name": self.name}


class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def walk(self):
        print(f"{self.name} is walking on four legs.")

    def to_dict(self):
        return {"type": "Mammal", "name": self.name, "fur_color": self.fur_color}


class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly

    def fly(self):
        if self.can_fly:
            print(f"{self.name} is flying.")
        else:
            print(f"{self.name} cannot fly.")

    def to_dict(self):
        return {"type": "Bird", "name": self.name, "can_fly": self.can_fly}


class Fish(Animal):
    def __init__(self, name, water_type):
        super().__init__(name)
        self.water_type = water_type

    def swim(self):
        print(f"{self.name} swims through {self.water_type} water.")

    def to_dict(self):
        return {"type": "Fish", "name": self.name, "water_type": self.water_type}


class Lion(Mammal):
    def make_sound(self):
        print(f"{self.name} roars!")

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Lion"
        return data


class Penguin(Bird):
    def swim(self):
        print(f"{self.name} is swimming.")

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Penguin"
        return data


class Cod(Fish):
    def swim(self):
        print(f"{self.name} swims along the seabed hunting for food.")

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Cod"
        return data
