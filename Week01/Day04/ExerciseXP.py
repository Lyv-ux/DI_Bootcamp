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






#🌟 Exercise 2: Dogs

class Dog:
    # Step 1
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    # Méthode pour aboyer
    def bark(self):
        return f"{self.name} is barking"

    # Méthode pour calculer la vitesse
    def run_speed(self):
        # Formule demandée : poids / âge * 10
        return (self.weight / self.age) * 10

    # Méthode pour simuler un combat entre deux chiens
    def fight(self, other_dog):
        # 1. On calcule la force du premier chien (self)
        self_force = self.run_speed() * self.weight
        
        # 2. On calcule la force du deuxième chien (other_dog)
        other_force = other_dog.run_speed() * other_dog.weight
        
        # 3. On compare les forces pour trouver le gagnant
        if self_force > other_force:
            return f"{self.name} won the fight against {other_dog.name}!"
        elif other_force > self_force:
            return f"{other_dog.name} won the fight against {self.name}!"
        else:
            return f"It's a tie between {self.name} and {other_dog.name}!"


# Step 2

# On crée 3 chiens avec des caractéristiques différentes
dog1 = Dog("Rex", age=3, weight=25)     
dog2 = Dog("Max", age=7, weight=15)      
dog3 = Dog("Rocky", age=2, weight=10)    


# Step 3

if __name__ == '__main__':
    # Test de bark()
    print(dog1.bark())  # Rex aboie
    
    # Test de run_speed()
    print(f"Max's speed: {dog2.run_speed():.2f}") 
    print(f"Rocky's speed: {dog3.run_speed():.2f}")
    
    print("--- FIIIGHT ! ---")
    # Test de fight() : Rex affronte Max
    print(dog1.fight(dog2))
    
    # Test de fight() : Max affronte Rocky
    print(dog2.fight(dog3))



    #🌟 Exercise 3: Dogs Domesticated

