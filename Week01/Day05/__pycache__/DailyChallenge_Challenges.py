#Challenge 1 : Sorting
#entree = input("Entrez des mots séparés par des virgules : ")

# 2. Découpage et tri via une compréhension de liste .split(",") dit à Python de séparer les mots à chaque fois qu'il voit une
#mots_tries = sorted([mot for mot in entree.split(",")])

# .join retourne le texte brut avec un séparateur au choix.
#resultat = ",".join(mots_tries)
#print(resultat)


#Challenge 2 : Longest Word
def find_longest_word(sentence):
    real_sentence = sentence.split(" ")
    
    # 1. On initialise le "champion" avec le tout premier mot
    plus_long_mot = real_sentence[0]
    
    # 2. On parcourt tous les mots de la phrase
    for mot in real_sentence:
        # Si le mot actuel est strictement plus long que notre champion...
        if len(mot) > len(plus_long_mot):
            # ...il devient le nouveau champion !
            plus_long_mot = mot
            
    # 3. L'énoncé demande de "retourner" (return) le mot, pas juste de l'imprimer
    return plus_long_mot

# Test
print(find_longest_word("Margaret's toy is a pretty doll."))
# Résultat : Margaret's