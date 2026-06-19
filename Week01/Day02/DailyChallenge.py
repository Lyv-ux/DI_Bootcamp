#Challenge 1
#-------------

# 1. User Input : On demande le mot à l'utilisateur
mot = input("Veuillez entrer un mot : ").strip()

# On crée un dictionnaire vide pour accumuler nos résultats
dictionnaire_indices = {}

# 2. Creating the Dictionary
# 'index' recevra le numéro (0, 1, 2...) et 'lettre' recevra le caractère ('d', 'o'...)
for index, lettre in enumerate(mot):
    
    # On vérifie si la lettre est déjà une clé du dictionnaire
    if lettre in dictionnaire_indices:
        # Si elle existe déjà, on ajoute (append) le nouvel index à sa liste
        dictionnaire_indices[lettre].append(index)
    else:
        # Si elle n'existe pas, on crée la clé avec une liste contenant le premier index
        dictionnaire_indices[lettre] = [index]

# 3. Expected Output : On affiche le dictionnaire final
print(dictionnaire_indices)





#Challenge 2
#------------
# 1. Stockage des données d'origine
items_purchase = {
    "Water": "$1", 
    "Bread": "$3", 
    "TV": "$1,000", 
    "Fertilizer": "$20"
}
wallet = "$300"

# 2. Nettoyage du portefeuille (Wallet)
# On remplace le '$' par du vide et on convertit en entier
wallet_clean = int(wallet.replace("$", ""))

# Création du panier vide
basket = []

# 3. Parcours du dictionnaire dans l'ordre de priorité
for item, price_str in items_purchase.items():
    
    # Nettoyage du prix de l'article (on enlève le '$' et la virgule ',')
    price_clean = price_str.replace("$", "").replace(",", "")
    price = int(price_clean)
    
    # Vérification : Est-ce qu'on a assez d'argent ?
    if price <= wallet_clean:
        basket.append(item)          # On ajoute l'article au panier
        wallet_clean -= price        # On met à jour l'argent restant dans le portefeuille

# 4. Détermination du résultat final
if len(basket) == 0:
    print("Nothing")
else:
    # On trie le panier par ordre alphabétique avant de l'afficher
    basket_sorted = sorted(basket)
    print(basket_sorted)
