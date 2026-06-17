#🌟 Exercise 1: Cats
#Step 1: Create Cat Objects
class Cat():
     def __init__(self, age, name):
         self.age = age
         self.name = name

     def __str__(self):
         return f"{self.name} {self.age}"

instance_1 = Cat(2, "Jul")        
instance_2 = Cat(4,"Chatty")
instance_3 = Cat(1, "Amy")

# #print(instance_1, instance_2, instance_3)

#Step 2: Create a Function to Find the Oldest Cat and Step 3: Print the Oldest Cat’s Details

def find_oldest_cat(cats):
    oldest_cat = cats[0]
    for cat in cats:
        if cat.age > oldest_cat.age :
            oldest_cat = cat
    print(f"The oldest cat is {oldest_cat.name}, it is {oldest_cat.age} years old")

find_oldest_cat([instance_1, instance_2, instance_3])



#🌟 Exercise 2 : Dogs
#Step 1: Create the Dog Class

class Dog():
    def __init__(self, name, height):
          self.name = name
          self.height = height
          #C'est Self.name et non Dog.name sinon ça prend la valeur de la dernière instance 
          #Et c'es la même chose pour toutes les fonctions dans des classes (méthodes)
    def bark(self):
            print(f"{self.name} goes woof!")
            #idem
    def jump(self):
            print(f"{self.name} jumps {self.height *2 }")
            #idem
    # def print_dog(self):
    #        print(f"The dog name is : {self.name} and its height is : {self.height}")
           #idem
   
#Step 2: Create Dog Objects
#Create davids_dog and sarahs_dog objects with their respective names and heights.
davids_dog = Dog ("Namy", 7)
sarahs_dog = Dog ("Raham", 2)

#Step 3: Print Dog Details and Call Methods
print(f"David's dog name is : {davids_dog.name} and its height is {davids_dog.height}")
print(f"Sarah's dog name is : {sarahs_dog.name} and its height is {sarahs_dog.height}")
davids_dog.jump()
davids_dog.bark()
sarahs_dog.jump()
sarahs_dog.bark()

#Step 4: Compare Dog Sizes

def compare_size(dog1, dog2):
    if dog1.height > dog2.height:
      print(f"Le chien ayant la plus grande taille est: {dog1.name}. Sa taille est : {dog1.height}")
    else:
      print(f"Le chien ayant la plus grande taille est: {dog2.name}. Sa taille est: {dog2.height}")

compare_size(davids_dog,sarahs_dog)


#🌟 Exercise 3 : Who’s the song producer?
#Step 1: Create the Song Class

class Song():
     # Attribut: ghu ="yeyt"
     def __init__(self, lyrics ):
          self.lyrics = lyrics

     def sing_me_a_song(self):
          for line in self.lyrics:
            print(line, end=" ")    
# C'est pendant le test qu'on lui fat omprendre que c'est une liste Pas au début
stairway = Song(["There's a lady who's sure", "all that glitters is gold", "and she's buying a stairway to heaven"])
stairway.sing_me_a_song()


#🌟 Exercise 4 : Afternoon at the Zoo
#--------------------------------------
# =====================================================================
# STEP 1: Définition de la classe Zoo
# =====================================================================
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []        # RECTIFIÉ : self.animals pour que le zoo s'en rappelle
        self.groups = {}         # On crée un dictionnaire vide pour stocker les groupes plus tard

    # 3. Ajouter un animal
    def add_animal(self, new_animal): # RECTIFIÉ : Ajout de self dans les parenthèses
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"-> {new_animal} a été ajouté au zoo.")
        else:
            print(f"-> {new_animal} est déjà dans le zoo !")

    # 4. Afficher tous les animaux
    def get_animals(self):
        print(f"\nAnimaux actuellement au zoo {self.zoo_name} :")
        for animal in self.animals:
            print(f"- {animal}")

    # 5. Vendre un animal (le supprimer de la liste)
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"-> {animal_sold} a été vendu.")
        else:
            print(f"-> Impossible de vendre {animal_sold}, il n'est pas dans le zoo.")

    # 6. Trier et regrouper les animaux par leur première lettre
    def sort_animals(self):
        # Étape A : On trie d'abord la liste principale par ordre alphabétique
        self.animals.sort()
        
        # On vide le dictionnaire des groupes pour le recalculer proprement
        self.groups = {}
        
        # Étape B : On parcourt chaque animal trié
        for animal in self.animals:
            premiere_lettre = animal[0] # On récupère la première lettre (ex: 'B' pour 'Bear')
            
            # Si cette lettre n'est pas encore un tiroir de notre dictionnaire
            if premiere_lettre not in self.groups:
                self.groups[premiere_lettre] = [animal] # On crée le tiroir avec une liste contenant l'animal
            else:
                self.groups[premiere_lettre].append(animal) # Le tiroir existe, on ajoute l'animal dedans

    # 7. Afficher les groupes créés par sort_animals
    def get_groups(self):
        print("\n--- Organisation des animaux par lettre ---")
        for lettre, liste_animaux in self.groups.items():
            print(f"{lettre}: {liste_animaux}")


# =====================================================================
# STEP 2 & 3: Création du zoo et tests des méthodes
# =====================================================================

# Création de notre zoo
brooklyn_safari = Zoo("Brooklyn Safari")

# Ajout des animaux
print("--- INSCRIPTION DES ANIMAUX ---")
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.add_animal("Cat")
brooklyn_safari.add_animal("Cougar")
brooklyn_safari.add_animal("Zebra")

# Affichage de contrôle
brooklyn_safari.get_animals()

# Vente d'un animal
print("\n--- VENTE D'UN ANIMAL ---")
brooklyn_safari.sell_animal("Bear")

# Vérification après la vente
brooklyn_safari.get_animals()

# Tri et regroupement
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()
   