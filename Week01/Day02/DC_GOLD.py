import re

# 1. Définition de la matrice brute sous forme de chaîne
matrix_str = """7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!"""

# Convertir la chaîne en une liste 2D (grille de caractères)
# Chaque ligne est une liste de caractères
grid = [list(line) for line in matrix_str.split('\n')]

rows = len(grid)
cols = len(grid[0])

# 2. Lecture par colonne (Verticalement)
raw_decoded_chars = []

for c in range(cols):
    for r in range(rows):
        raw_decoded_chars.append(grid[r][c])

# On fusionne tous les caractères lus verticalement en une seule chaîne
full_string = "".join(raw_decoded_chars)

# 3. Nettoyage avec les Expressions Régulières (RegEx)
# On cherche les groupes de caractères non-alphanumériques ([^a-zA-Z0-9]+)
# qui se trouvent ENTRE deux caractères alphanumériques (?<=\w) ... (?=\w)
# et on les remplace par un espace.

# Note : On utilise \w pour cibler l'alphanumeric standard.
cleaned_message = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', full_string)

# Enfin, on retire les symboles restants aux extrémités (comme le '!' ou '^' à la fin)
# pour ne garder que le texte propre.
final_message = re.sub(r'[^\w\s]', '', cleaned_message).strip()

# 4. Affichage du résultat
print("Message secret décodé :")
print(f"👉 {final_message}")