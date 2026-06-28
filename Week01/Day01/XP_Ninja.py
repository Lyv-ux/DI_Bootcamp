#📝 Exercise 1 : Outputs


#Predict the output of the following code snippets:



3 <= 3 < 9       #--> True

#3 == 3 == 3     #--> True

bool(0)          #--> False

bool(5 == "5")   #--> False

bool(4 == 4) == bool("4" == "4")  #--> True

bool(bool(None))   #--> False

x = (1 == True) 
y = (1 == False)
a = True + 4
b = False + 10

print("x is True", x)
print("y is False", y)
print("a: ", 5)
print("b: ", 10)




#Exercice 2 : Longest word without a specific character
def defi_sans_lettre_a():
    longueur_max = 0
    print("--- Bienvenue au défi de la phrase sans la lettre 'A' ou 'a' ! ---")
    print("(Tapez 'quitter' pour arrêter le jeu)\n")
    
    while True:
        phrase = input("Entrez la plus longue phrase possible sans la lettre 'A' : ")
        
        if phrase.lower() == 'quitter':
            print("Merci d'avoir joué !")
            break
            
        # Vérification de la présence de la lettre 'A'
        if 'a' in phrase.lower():
            print("Perdu ! Cette phrase contient la lettre 'A'. Réessayez.\n")
        else:
            longueur_actuelle = len(phrase)
            if longueur_actuelle > longueur_max:
                longueur_max = longueur_actuelle
                print(f"Félicitations ! Nouveau record établi avec {longueur_max} caractères !")
                print(f"Phrase : \"{phrase}\"\n")
            else:
                print(f"C'est correct (sans 'A'), mais trop court. Votre record actuel est de {longueur_max} caractères.\n")

# Lancer le jeu :
#defi_sans_lettre_a()




#Exercice 3

import re

# Paragraphe choisi
paragraphe = (
    "We die. That may be the meaning of life. But we do language. "
    "That may be the measure of our lives. Word-work is sublime because it is generative; "
    "it makes meaning that secures our difference, our human difference, the way in which "
    "we are like no other life."
)


# 1. Nombre total de caractères
total_caracteres = len(paragraphe)

# 2. Nombre de phrases (on découpe selon les '.', '!' ou '?')
# On filtre les éléments vides générés par le split en fin de chaîne
phrases = [p.strip() for p in re.split(r'[.!?]', paragraphe) if p.strip()]
nombre_phrases = len(phrases)

# 3. Nombre de mots
# re.findall(r'\b\w+\b', ...) extrait tous les mots en ignorant la ponctuation pure
mots = re.findall(r'\b\w+\b', paragraphe.lower())
nombre_mots = len(mots)

# 4. Nombre de mots uniques (utilisation d'un set pour éliminer les doublons)
mots_uniques = set(mots)
nombre_mots_uniques = len(mots_uniques)

# --- BONURS ---

# Bonus 1 : Nombre de caractères sans les espaces
caracteres_sans_espace = len(paragraphe.replace(" ", ""))

# Bonus 2 : Nombre moyen de mots par phrase
moyenne_mots_par_phrase = nombre_mots / nombre_phrases if nombre_phrases > 0 else 0

# Bonus 3 : Nombre de mots non uniques (les mots qui apparaissent plus d'une fois)
# On soustrait le nombre de mots uniques du nombre total de mots
nombre_mots_non_uniques = nombre_mots - nombre_mots_uniques



print("====== ANALYSE TEXTUELLE ======\n")
print(f"• Nombre total de caractères : {total_caracteres}")
print(f"• Nombre de caractères (sans espaces) [Bonus] : {caracteres_sans_espace}")
print(f"• Nombre de phrases : {nombre_phrases}")
print(f"• Nombre total de mots : {nombre_mots}")
print(f"• Nombre de mots uniques : {nombre_mots_uniques}")
print(f"• Nombre de mots répétés (non uniques) [Bonus] : {nombre_mots_non_uniques}")
print(f"• Moyenne de mots par phrase [Bonus] : {moyenne_mots_par_phrase:.2f} mots/phrase")
print("\n===============================")