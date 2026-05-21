#EXERCICE 1
#----------
#You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
# Conversion directe en dictionnaire
mon_dictionnaire = dict(zip(keys, values))
print(mon_dictionnaire)






#EXERCICE 2
#-------------
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# Un dictionnaire avec les membres et leurs âges
cout_total = 0

# 1. BOUCLE DE DICTIONNAIRE : on extrait le membre (clé) et l'âge (valeur)
for membre, age in family.items():
    
    # 2. CONDITIONS & OPÉRATIONS LOGIQUES
    if age < 3:
        prix_ticket = 0
        print(f"Ticket pour {membre} ({age} ans) : Free")
        
    elif age >= 3 and age <= 12:  # Utilisation de l'opération logique 'and'
        prix_ticket = 10
        print(f"Ticket pour {membre} ({age} ans) : $10")
        
    else:
        prix_ticket = 15
        print(f"Ticket pour {membre} ({age} ans) : $15")
        
    # Accumulation dans le coût total
    cout_total += prix_ticket

print(f"Total cost for the family: ${cout_total}")




#EXERCICE 3
#-----------
#a_Create a dictionary called brand with the provided data.
brand = {

    "name": "Zara",
    "creation_date": 1975,
    "creator_name": 'Amancio Ortega Gaona',
    "type_of_clothes" : ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
     "number_stores": 7000,
     "major_color": [ "France: blue", "Spain: red", "US: pink, green"]
}

#b_Change the value of number_stores to 2.
brand['number_stores'] = 2
print(brand)

#c_Print a sentence describing Zara’s clients using the type_of_clothes key.
print (f"Zara's Clients are {brand['type_of_clothes']}") 

#d_Add a new key country_creation with the value Spain.
nouvelle_cle  = {"country_creation ": "Spain"}
# Ajout avec .update()
brand.update(nouvelle_cle)
print(brand)

#e_Check if international_competitors exists and, if so, add “Desigual” to the list.
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
print(brand)  
  
#f_Delete the creation_date key.
brand.pop("creation_date")
print(brand)    

#g_Print the last item in international_competitors.
print(brand["international_competitors"][-1])

#h_Print the major colors in the US.
print(brand["major_color"][-1])

#i_Print the number of keys in the dictionary.
nbre = len(brand)
print(f"Le nombre de clés de brand est: {nbre}")

#j_Print all keys of the dictionary.
for cle in brand:
    print(cle)

#BONUS
more_on_zara = {
    "creation_date": None,
    "number_stores" : None
}
brand.update(more_on_zara)
print(brand)



#🌟 Exercise 4 : Some Geography
#-------------------------------
#Step 1: Define a Function with Parameters
def describe_city(city, country = "Unknown"):

#Step 2: Print a Message
    print(city +" is in " + country)

#Step 3: Call the Function
describe_city("Abidjan", "Cote d'Ivoire")
describe_city("Seoul")


#🌟 Exercise 5 : Random
#------------------------
#Step 1: Import the random Module
import random
#Step 2: Define a Function with a Parameter
def Comparer_nombre (nombre_utilisateur):
#Step 3: Generate a Random Number
    random_number = random.randint(1, 100)
    # Step 4: Compare the Numbers
    if nombre_utilisateur == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {nombre_utilisateur}, Random number: {random_number}")
# Step 5: Call the Function
Comparer_nombre(100)




#🌟 Exercise 6 : Let’s create some personalized shirts !
#---------------------------------------------------------
#Step 1: Define a Function with Parameters
def make_shirt(size ="large",text = "I love Python."):
#Step 2: Print a Summary Message
     print(f"The t-shirt size is {size} and the text on it is {text}")
#Step 3: Call the Function and Step 4: Modify the Function with Default Values
#Step 5: Call the Function with Default and Custom Values
make_shirt()
make_shirt("medium")
make_shirt("small", "I'm getting better and betteeer every single day.")
#Step 6 (Bonus): Keyword Arguments
make_shirt(text="Smooth Criminal", size="Xl")


#🌟 Exercise 7 : Temperature Advice
#Step 1: Create the get_random_temp() Function
def get_random_temp():
     return random.randint(-10, 40)
#Step 2: Create the main() Function
def main():
    get_random_temp()
    var = get_random_temp()
    print(f"The temperature right now is {var} degrees Celsius.")
    return var
#main()
#Step 3: Provide Temperature-Based Advice
temperature = main()
if temperature < 0:
    print("Brrr, that's freezing! Wear some extra layers today")
elif temperature >= 0 and temperature <= 16:
    print("Quite chilly! Don't forget your coat.")
if temperature > 16 and temperature <= 23:
    print("Nice weather.")
elif temperature >= 23 and temperature <= 31:
    print("A bit warm, stay hydrated.")
if temperature >= 32 and temperature <= 40:
    print("It's really hot! Stay cool.")
#Step 4: Floating-Point Temperatures (Bonus)



#🌟 Exercise 8: Pizza Toppings
#-------------------------------
# 1. Initialisation des variables
toppings = []  # Liste vide pour stocker les ingrédients
base_price = 10.0
price_per_topping = 2.50

print("--- Bienvenue au configurateur de Pizza ! ---")
print("Entrez vos ingrédients un par un (ou tapez 'quit' pour terminer) :\n")

# 2. La boucle d'écoute de l'utilisateur
while True:
    choix = input("Quel ingrédient voulez-vous ajouter ? : ").strip().lower()
    
    # Condition d'arrêt
    if choix == 'quit':
        break
        
    # Validation : on évite d'ajouter une entrée vide si l'utilisateur appuie juste sur Entrée
    if choix == "":
        print("Veuillez entrer un ingrédient valide.")
        continue
        
    # Ajout de l'ingrédient à la liste et message de confirmation
    toppings.append(choix)
    print(f"-> Adding {choix} to your pizza.")

# 3. Calculs finaux après la sortie de la boucle
total_cost = base_price + (len(toppings) * price_per_topping)

# 4. Affichage du résumé
print("\n--------------------------------------------------")
print("RÉSUMÉ DE VOTRE COMMANDE :")

if toppings:
    # On affiche les ingrédients proprement séparés par une virgule
    print(f"Vos ingrédients : {', '.join(toppings)}")
else:
    print("Vos ingrédients : Aucune garniture (Pizza nature)")

# String formatting pour afficher le prix avec deux décimales ($XX.XX)
print(f"Total cost of the pizza: ${total_cost:.2f}")
print("--------------------------------------------------")