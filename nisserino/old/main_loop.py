import background as bg

daycare = bg.Dog_daycare("Vacker Tass", "Nisse")
input_options = [
    "help", "show dogs",  "add dog", "remove dog",
    "dog.conf", "change boss", "quit"
    ]
conf_options = [
    "help", "stats", "owner", "favtoy", "age",
    "name", "breed", "bff", "go back", "change dog"
    ]
print(
    f"Welcome to the daycare {daycare.name}!\n What would you like to do?\n"
    "You can add dogs, their breeds, best friends and much more\n"
    "To see all your options, write 'help'"
)
while True:
    usr_input = bg.text_input()
    if usr_input not in input_options:
        print("\nDid you write that correctly?\nWrite 'help' to see options")
    else:
        if usr_input == "help":
            print(input_options)
        elif usr_input == "show dogs":
            daycare.all_dogs()
        elif usr_input == "add dog":
            name, age, owner = bg.dog_init()
            daycare.add_dog(name, age, owner)
        elif usr_input == "remove dog":
            print("Who do you wish to remove from the daycare?")
            to_remove = daycare.find_dog(bg.text_input())
            if to_remove is not None:
                daycare.remove_dog(to_remove)
            else:
                print("We couldn't find that dog\n")
        elif usr_input == "change boss":
            print("Who's the new boss?")
            daycare.set_boss_name(bg.text_input())
        elif usr_input == "quit":
            break
        elif usr_input == "dog.conf":
            print("What dog would you like to configure?")
            dog = daycare.find_dog(bg.text_input())
            while True:
                print(f"Your options are: {conf_options}")
                usr_input = bg.text_input()
                if usr_input not in conf_options:
                    print("Did you spell correctly?")
                else:
                    if usr_input == "stats":
                        dog.show_stats()
                    elif usr_input == "name":
                        print(f"Changing {dog.name}s name to ...")
                        dog.set_name(bg.text_input())
                    elif usr_input == "owner":
                        print(f"Changing owner {dog.owner} to ...")
                        dog.set_owner(bg.text_input())
                    elif usr_input == "favtoy":
                        print(f"Changing favourite toy from {dog.toy} to ...")
                        dog.set_toy(bg.text_input())
                    elif usr_input == "age":
                        print(f"Changing age from {dog.age} to ...")
                        dog.set_age(bg.int_input())
                    elif usr_input == "breed":
                        print(f"Changing breed from {dog.breed} to ...")
                        dog.set_breed(bg.text_input())
                    elif usr_input == "go back":
                        break
                    elif usr_input == "bff":
                        print(f"Changing bff from {dog.bff} to ...")
                        dog.add_bff(daycare.find_dog(bg.text_input()))
                    elif usr_input == "help":
                        print(f"Your options are: {conf_options}")
                    elif usr_input == "change dog":
                        print("What dog would you like to configure?")
                        dog = daycare.find_dog(bg.text_input())
