import cmd
import background as bg

daycare = bg.Dog_daycare("Vacker Tass", "Nisse")


class Daycare_loop(cmd.Cmd):
    intro = "Welcome to the daycare"
    prompt = "(Admin): "

    def do_show_dogs(self, arg):
        'Show the names of all dogs in the daycare'
        daycare.show_dogs()

    def do_show_dogs_all(self, arg):
        'Shows all info about all dogs in the daycare'
        print("Pranked!")

    def do_add_dog(self, arg):
        'Add a dog: add_dog name,age,owner'
        daycare.add_dog(arg)

    def do_remove_dog(self, arg):
        'Remove a dog: remove_dog dog_name'
        daycare.remove_dog(daycare, arg)

    def do_stats(self, arg):
        'Show specific dogs stats: stats dog_name'
        bg.show_stats(daycare, arg)

    def do_dog_name(self, arg):
        'Change dog name: dog_name name, newname'
        bg.set_name(daycare, arg)

    def do_dog_owner(self, arg):
        'Change dog owner: dog_owner dog_name, new_owner'
        bg.set_owner(daycare, arg)

    def do_dog_toy(self, arg):
        'Change dog toy: dog_name, toy'
        bg.set_toy(daycare, arg)

    def do_dog_age(self, arg):
        'Change dog age: dog_name, age'
        bg.set_age(daycare, arg)

    def do_dog_breed(self, arg):
        'Change dog breed: dog_name, dog_breed'
        bg.set_breed(daycare, arg)

    def do_dog_bff(self, arg):
        'Add dogs bff: dog_bff dog_name, bffs_name'
        bg.add_bff(daycare, arg)

    def do_daycare_name(self, arg):
        'Change the name of the daycare: daycare_name new_name'
        daycare.set_daycare_name(arg)

    def do_daycare_boss(self, arg):
        'Change boss to a new one: change_boss name'
        daycare.set_boss_name(arg)

    def do_daycare_info(self, arg):
        'Show info about the daycare'
        daycare.show_daycare_info()

    def do_quit(self, arg):
        'Exit the program'
        return True


Daycare_loop().cmdloop()
