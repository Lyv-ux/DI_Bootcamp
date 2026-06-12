#Exercises 1 and 2
#Create a variable called birthdays. Its value should be a dictionary and Initialize this variable with the birthdays of 5 people of your choice. For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday. Tip: Use the format "YYYY/MM/DD".

# On initialise le dictionnaire avec 5 personnes de notre choix
birthdays = {
    "Lara Croft": "1992/02/14",
    "Luke Skywalker": "1977/05/25",
    "Tony Stark": "1970/05/29",
    "Bruce Wayne": "1915/04/17",
    "Princess Zelda": "1986/02/21"
}

print("✨ Bienvenue dans l'application de recherche d'anniversaires ! ✨")
print("Vous pouvez consulter l'anniversaire des personnes suivantes :\n")






# Exercice 2 : On affiche d'abord tous les noms disponibles
for name in birthdays.keys():
    print(f"- {name}")

print("-" * 40)

# On demande le nom à l'utilisateur
search_name = input("Entrez le nom d'une personne pour connaître sa date de naissance : ").strip()

# Exercice 2 : Gestion d'erreur si le nom n'existe pas
if search_name in birthdays:
    # Exercice 1 : Récupération et affichage formaté
    birthday_date = birthdays[search_name]
    print(f"🎉 L'anniversaire de {search_name} est le : {birthday_date}")
else:
    print(f"❌ Sorry, we don’t have the birthday information for {search_name}.")

    #Exercise 3
    names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name = input("Entrez un nom de personnage : ").strip()

# On vérifie si le nom est présent dans la liste pour éviter une erreur Python
if user_name in names:
    first_index = names.index(user_name)
    print(f"Le personnage '{user_name}' a été trouvé ! Premier index : {first_index}")
else:
    print(f"Le nom '{user_name}' n'est pas dans la liste.")



    #Exercice 4

    import random

def throw_dice():
    """Simule le lancer d'un dé à 6 faces."""
    return random.randint(1, 6)


def throw_until_doubles():
    """Lance deux dés jusqu'à obtenir un double et renvoie le nombre de tentatives."""
    attempts = 0
    while True:
        dice1 = throw_dice()
        dice2 = throw_dice()
        attempts += 1
        
        # Si on obtient un double, on arrête la boucle
        if dice1 == dice2:
            return attempts


def main():
    # Collection pour stocker le nombre de lancers nécessaires pour chaque double
    results = []
    
    # On cherche à obtenir 100 doubles
    for _ in range(100):
        attempts_needed = throw_until_doubles()
        results.append(attempts_needed)
    
    # Calculs statistiques
    total_throws = sum(results)
    average_throws = total_throws / len(results)
    
    # Affichage des résultats
    print("🎲 --- Résultats de la simulation (100 doubles) --- 🎲")
    print(f"Total throws: {total_throws}")
    print(f"Average throws to reach doubles: {average_throws:.2f}")

# Exécution du programme de simulation
if __name__ == "__main__":
    main()