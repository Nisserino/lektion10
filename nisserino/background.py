class Dog():
    id = 0

    def __init__(self, name, age, owner):
        self.name = name
        self.age = age
        self.owner = owner
        self.breed = "Unknown"
        self.toy = "Unknown"
        self.bff = []
        Dog.id += 1
        self.id = Dog.id

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_owner(self, owner):
        self.owner = owner

    def set_breed(self, breed):
        self.breed = breed

    def set_toy(self, toy):
        self.toy = toy

    def add_bff(self, bff):
        if self.breed == "golden retriever":
            self.bff.append(bff)
        else:
            self.bff = [bff]

    def show_stats(self):  # Make printout prettier (not a priority)
        print(
            f"\nId: {self.id}"
            f"\nName: {self.name}\tAge: {self.age}\tOwner: {self.owner}\n"
            f"Breed: {self.breed}\tFavourite toy: {self.toy}"
        )
        if self.breed == "golden retriever":
            friends = []
            for self in self.bff:
                friends.append(self.name)
            print(f"Bff(s){friends}")
        elif self.bff:
            print(f"Bff: {self.bff[0].name}\n")
        else:
            print(f"{self.name} has no best friend yet.\n")


class Dog_daycare:
    def __init__(self, name, boss):
        self.name = name
        self.boss = boss
        self.dogs = []

    def set_name(self, name):
        self.name = name

    def set_boss_name(self, boss):
        self.boss = boss

    def add_dog(self, name, age, owner):
        dog_add = Dog(name, age, owner)
        self.dogs.append(dog_add)

    def find_dog(self, name):
        for dog in self.dogs:
            if dog.name == name:
                return dog

    def remove_dog(self, dog):
        self.dogs.remove(dog)

    def show_dogs(self):
        for dog in self.dogs:
            print(dog.name)


def text_input():
    try:
        text = input("\n: ").strip().lower()
        return text
    except Exception as e:
        print(f"error: {e}")


def int_input():
    while True:
        try:
            number = int(input(": "))
            return number
            break
        except ValueError:
            print("Enter an integer")
        except Exception as e:
            print(f"Error: {e}")


def dog_init():
    while True:
        try:
            name = input("Enter dogs name\n: ").strip().lower()
            age = int(input("Enter dogs age\n: "))
            owner = input("Enter the owners name\n: ").strip().lower()
            break
        except ValueError:
            print("You need to enter an integer for the age\n")
        except Exception as e:
            print(f"Error: {e}")
    return name, age, owner


def daycare_init():  # Fix inputs later
    name = input("Enter the name of the daycare\n:")
    boss = input("Enter the boss name\n: ")
    return(name, boss)
