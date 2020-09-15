import cmd
from background import *

daycare = Dog_daycare("Vacker Tass", "Nisse")


class Daycare_loop(cmd.Cmd):
    into = "Welcome to the daycare"
    prompt = "(Daycare): "
    file = None

    def do_show_dogs(self, arg):
        'Show the names of all dogs in the Day-care!'
        try:
            daycare.all_dogs()
        except Exception as e:
            print(f"Error: {e}")

    def do_add_dog(self, arg):  # Fix strip in some sense
        'Add a dog: add_dog name,age,owner'
        try:
            name, age, owner = arg.split(",")
            daycare.add_dog(name.lower().strip(), int(age), owner.lower().strip())
        except Exception as e:
            print(f"Error: {e}")

    def do_remove_dog(self, dog):  # Add option to remove by id/owner/age
        'Remove a dog: remove_dog dog_name'
        try:
            daycare.remove_dog(daycare.find_dog(dog))
        except Exception as e:
            print(f"Error {e}")

    def do_change_boss(self, arg):
        'Change boss to a new one: change_boss name'
        try:
            daycare.set_boss_name(arg)
        except Exception as e:
            print(f"Error: {e}")

    def do_stats(self, dog):
        'Show specific dogs stats: stats dog_name'
        try:
            daycare.find_dog(dog).show_stats()
        except Exception as e:
            print(f"Error: {e}")

    def do_dog_name(self, arg):
        'Change dog name: dog_name name, newname'
        try:
            dog, new_name = arg.split(",")
            daycare.find_dog(dog.lower().strip()).set_name(new_name.lower().strip())
        except Exception as e:
            print(f"Error: {e}")

    def do_dog_owner(self, arg):
        'Change dog owner: dog_owner dog_name, new_owner'
        try:
            dog, new_owner = arg.split(",")
            daycare.find_dog(dog.lower().strip()).set_owner(new_owner.lower().strip())
        except Exception as e:
            print(f"Error: {e}")

    def do_dog_toy(self, arg):
        'Change dog toy: dog_name, toy'
        try:
            dog, toy = arg.split(",")
            daycare.find_dog(dog.lower().strip()).set_toy(toy.lower().strip())
        except Exception as e:
            print(f"Error: {e}")

    def do_dog_age(self, arg):
        'Change dog age: dog_name, age'
        try:
            dog, new_age = arg.split(",")
            daycare.find_dog(dog.lower().strip()).set_age(int(new_age))
        except Exception as e:
            print(f"Error: {e}")

    def do_dog_breed(self, arg):
        'Change dog breed: dog_name, dog_breed'
        try:
            dog, breed = arg.split(",")
            daycare.find_dog(dog.lower().strip()).set_breed(breed.lower().strip())
        except Exception as e:
            print(f"Error: {e}")

    def do_dog_bff(self, arg):
        'Add dogs bff: dog_bff dog_name, bffs_name'
        try:
            dog, bff = arg.split(",")
            daycare.find_dog(dog.lower().strip()).add_bff(daycare.find_dog(bff.lower().strip()))
        except Exception as e:
            print(f"Error: {e}")

    def do_quit(self, arg):
        'Exit the program'
        return True


Daycare_loop().cmdloop()
