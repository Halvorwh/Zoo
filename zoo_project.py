

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def make_sound(self):
        print(f"{self.name} makes a sound.")
        


class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        # think: you need to call Animal's __init__ too, to set self.name
        # hint: super().__init__(name)
        self.fur_color = fur_color

    def walk(self):
        print(f"{self.name} is walking on four legs.")


class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly


    def fly(self):
        if self.can_fly:
            print(f"{self.name} is flying.")
        else:
            print(f"{self.name} cannot fly.")
            
class Fish(Animal):
    def __init__(self, name, water_type):
        super().__init__(name)
        self.water_type = water_type

    def swim(self):
        print(f"{self.name} swims through {self.water_type} water.")




class Lion(Mammal):
    def make_sound(self):
        print(f"{self.name} roars!")


class Penguin(Bird):
    def swim(self):
        print(f"{self.name} is swimming.")
        
class Cod(Fish):
    def water_type(self):
        print(f"{self.name} is without sound")


# test it out
leo = Lion("Leo", "golden")
leo.eat()          # inherited from Animal
leo.walk()         # inherited from Mammal
leo.make_sound()   # Lion's own version — overrides Animal's generic one

pingo = Penguin("Pingo", False)
pingo.eat()      # inherited from Animal
pingo.fly()      # inherited from Bird — should print "cannot fly"
pingo.swim()     # Penguin's own method

lofottorsk = Fish("Lofottorsk", "salt")
lofottorsk.eat()     # inherited from Animal
lofottorsk.swim()    # Fish's own method — no .fly(), Fish never inherited that




