import json
from animals import Lion, Penguin, Cod, Mammal, Bird, Fish

ANIMAL_CLASSES = {
    "Lion": Lion,
    "Penguin": Penguin,
    "Cod": Cod,
}

zoo = []

def save_zoo():
    data = [animal.to_dict() for animal in zoo]
    with open("zoo.json", "w") as file:
        json.dump(data, file)

def load_zoo():
    global zoo
    try:
        with open("zoo.json", "r") as file:
            data = json.load(file)
            zoo = []
            for entry in data:
                animal_type = entry["type"]
                cls = ANIMAL_CLASSES.get(animal_type)
                if cls is None:
                    continue

                if animal_type == "Lion":
                    zoo.append(cls(entry["name"], entry["fur_color"]))
                elif animal_type == "Penguin":
                    zoo.append(cls(entry["name"], entry["can_fly"]))
                elif animal_type == "Cod":
                    zoo.append(cls(entry["name"], entry["water_type"]))
    except FileNotFoundError:
        zoo = []

def list_animals():
    if not zoo:
        print("No animals yet.")
    else:
        for i, animal in enumerate(zoo, start=1):
            print(f"{i}. {animal.name} ({type(animal).__name__})")

def choose_animal():
    list_animals()
    if not zoo:
        return None
    try:
        index = int(input("Enter the animal number: ")) - 1
    except ValueError:
        print("Please enter a valid number.")
        return None
    if 0 <= index < len(zoo):
        return zoo[index]
    else:
        print("Invalid animal number.")
        return None

def add_animal():
    print("1. Lion")
    print("2. Penguin")
    print("3. Cod")
    choice = input("What kind of animal? ")

    name = input("Name: ")

    if choice == "1":
        fur_color = input("Fur color: ")
        zoo.append(Lion(name, fur_color))
    elif choice == "2":
        can_fly_input = input("Can it fly? (y/n): ").strip().lower()
        can_fly = can_fly_input == "y"
        zoo.append(Penguin(name, can_fly))
    elif choice == "3":
        water_type = input("Water type (salt/fresh): ")
        zoo.append(Cod(name, water_type))
    else:
        print("Invalid choice.")
        return

    print(f"{name} added to the zoo.")


load_zoo()

while True:
    print("\n1. Add animal")
    print("2. List animals")
    print("3. Feed animal (eat)")
    print("4. Make sound")
    print("5. Special action (walk/fly/swim)")
    print("6. Exit")

    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        add_animal()
        save_zoo()
    elif choice == 2:
        list_animals()
    elif choice == 3:
        animal = choose_animal()
        if animal:
            animal.eat()
    elif choice == 4:
        animal = choose_animal()
        if animal:
            animal.make_sound()
    elif choice == 5:
        animal = choose_animal()
        if animal:
            if isinstance(animal, Mammal):
                animal.walk()
            elif isinstance(animal, Bird):
                animal.fly()
            elif isinstance(animal, Fish):
                animal.swim()
    elif choice == 6:
        break
    else:
        print("Invalid option, try again.")
