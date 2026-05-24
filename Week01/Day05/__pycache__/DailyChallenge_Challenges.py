#Challenge 1 : Sorting
entree = input("Entrez des mots séparés par des virgules : ")

# 2. Découpage et tri via une compréhension de liste .split(",") dit à Python de séparer les mots à chaque fois qu'il voit une
mots_tries = sorted([mot for mot in entree.split(",")])

# .join retourne le texte brut avec un séparateur au choix.
resultat = ",".join(mots_tries)
print(resultat)


#Challenge 2 : Longest Word
def find_longest_word(sentence):
    real_sentence = sentence.split(" ")
    
    plus_long_mot = real_sentence[0]
    
    for mot in real_sentence:
        if len(mot) > len(plus_long_mot):
            plus_long_mot = mot
            
    return plus_long_mot


print(find_longest_word())
