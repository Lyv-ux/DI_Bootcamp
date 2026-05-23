# 🌟 Exercise 1: Pets

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'



# Step 1: Create the Siamese Class

class Siamese(Cat):
    pass


# Step 2: Create a List of Cat Instances

bengal_obj = Bengal("Garfield", 3)
chartreux_obj = Chartreux("Tom", 5)
siamese_obj = Siamese("Luna", 2)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]


# Step 3: Create a Pets instance of the list of cat instances
sara_pets = Pets(all_cats)


# Step 4: Take cats for a walk
sara_pets.walk()



