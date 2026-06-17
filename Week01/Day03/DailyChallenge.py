class Farm:
    # Étape 2 : On prépare le nom et le dictionnaire vide
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}  # Stockera par exemple : {'cow': 5, 'sheep': 2}

    # Étape 3 : Ajouter un animal
    def add_animal(self, animal_type, count=1):
        # Si l'animal est déjà dans le dictionnaire, on augmente sa quantité
        if animal_type in self.animals:
            self.animals[animal_type] = self.animals[animal_type] + count
        # Sinon, c'est la première fois qu'on le voit, on l'enregistre
        else:
            self.animals[animal_type] = count

    # Étape 4 : Créer le texte à afficher
    def get_info(self):
        # On commence à écrire la phrase du titre
        message = f"{self.name}'s farm\n"
        
        # On parcourt le dictionnaire pour ajouter chaque animal au message
        for animal, quantite in self.animals.items():
            message = message + f"{animal} : {quantite}\n"
            
        # On ajoute le cri de la ferme à la toute fin
        message = message + "    E-I-E-I-0!"
        return message


# =====================================================================
# Étape 5 
# =====================================================================

# 1. On crée la ferme
macdonald = Farm("McDonald")

# 2. On ajoute les animaux
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')  # Pas de nombre précisé, donc il ajoute 1 par défaut
macdonald.add_animal('sheep')  # Il rajoute encore 1 (le total des sheeps passera à 2)
macdonald.add_animal('goat', 12)

# 3. On affiche le résultat
print(macdonald.get_info())