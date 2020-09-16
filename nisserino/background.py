class Dog():
    identifier = 0

    def __init__(self, name, age, owner):
        self.name = name
        self.age = age
        self.owner = owner
        self.breed = "Unknown"
        self.toy = "Unknown"
        self.bff = []
        Dog.identifier += 1
        self.id = Dog.identifier


def set_name(daycare, arg):
    try:
        dog_name, new_name = parse(arg)
        dog = daycare.find_dog(daycare, dog_name)
        dog.name = new_name
    except Exception as e:
        print(f"Error: {e}")


def set_age(daycare, arg):
    try:
        dog_name, age = parse(arg)
        dog = daycare.find_dog(daycare, dog_name)
        dog.age = age
    except Exception as e:
        print(f"Error: {e}")


def set_owner(daycare, arg):
    try:
        dog_name, new_owner = parse(arg)
        dog = daycare.find_dog(daycare, dog_name)
        dog.owner = new_owner
    except Exception as e:
        print(f"Error: {e}")


def set_breed(daycare, arg):
    try:
        dog_name, breed = parse(arg)
        dog = daycare.find_dog(daycare, dog_name)
        dog.breed = breed
    except Exception as e:
        print(f"Error: {e}")


def set_toy(daycare, arg):
    try:
        dog_name, toy = parse(arg)
        dog = daycare.find_dog(daycare, dog_name)
        dog.toy = toy
    except Exception as e:
        print(f"Error: {e}")


def add_bff(daycare, arg):
    try:
        dog_name, bff = parse(arg)
        dog = daycare.find_dog(daycare, dog_name)
        bff = daycare.find_dog(daycare, bff)
        if dog.breed == "golden retriever":
            dog.bff.append(bff)
        else:
            dog.bff = [bff]
    except Exception as e:
        print(f"Error: {e}")


# Make print prettier
def show_stats(daycare, dog):
    try:
        if isinstance(dog, str):
            dog_obj = daycare.find_dog(daycare, dog)
        else:
            dog_obj = dog
        if dog_obj is not False:
            print(
                f"\nId: {dog_obj.id}"
                f"\nName: {dog_obj.name}\tAge: {dog_obj.age}\t"
                f"Owner: {dog_obj.owner}\n"
                f"Breed: {dog_obj.breed}\tFavourite toy: {dog_obj.toy}"
            )
            if dog_obj.breed == "golden retriever":
                friends = []
                for dog_obj in dog_obj.bff:
                    friends.append(dog_obj.name)
                print(f"Bff(s){friends}")
            elif dog_obj.bff:
                print(f"Bff: {dog_obj.bff[0].name}\n")
            else:
                print(f"{dog_obj.name} has no best friend yet.\n")
    except Exception as e:
        print(f"Error: {e}")


class Dog_daycare:
    def __init__(self, name, boss):
        self.name = name
        self.boss = boss
        self.dogs = []

    def set_daycare_name(self, name):
        self.name = name

    def set_boss_name(self, boss):
        self.boss = boss

    def add_dog(self, arg):
        try:
            name, age, owner = parse(arg)
            dog_add = Dog(name, int(age), owner)
            self.dogs.append(dog_add)
        except Exception as e:
            print(f"Error: {e}")

    def find_dog(self, daycare, name):  # Do I really need this in the class?
        dogs = []
        for dog in daycare.dogs:
            if dog.name == name:
                dogs.append(dog)
        if len(dogs) > 1:
            print(
                "We found more than one dog of that name"
                "Help us figure out which one you ment!"
                )
            for dog in dogs:
                show_stats(daycare, dog)

            identifier = parse(input(
                "Please select a dog by its id\n"
                "If you want to go back, write 0\n: "
                ))
            if identifier == 0:
                print("Nothing's changed\nGoing back")
                return False
            else:
                for i, dog in enumerate(dogs):
                    if dog.id == identifier:
                        return dogs[i]
                else:
                    print("We couldn't find that id")
                    return False
        elif len(dogs) == 1:
            return dogs[0]
        else:
            print("We couldn't find that dog")
            return False

    def remove_dog(self, daycare, dog_name):
        try:
            dog = daycare.find_dog(daycare, dog_name)
            daycare.dogs.remove(dog)
        except Exception as e:
            print(f"Error: {e}")
        # self.dogs.remove(dog)

    def show_dogs(self):
        for dog in self.dogs:
            print(f"{dog.name}\t\t| Id: {dog.id}")

    def show_daycare_info(self):
        print(
            f"Daycare name: {self.name.title()}\n"
            f"Daycare boss: {self.boss.title()}\n"
            f"Amount of dogs enrolled: {len(self.dogs)}"
        )


def fix_input(arg):
    try:
        return int(arg)
    except ValueError:
        return arg.lower().strip()


def parse(arg):
    try:
        if "," in arg:
            return tuple(map(fix_input, arg.split(",")))
        else:
            return fix_input(arg)
    except Exception as e:
        print(f"Error: {e}")
