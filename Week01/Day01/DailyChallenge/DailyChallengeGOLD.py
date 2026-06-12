from datetime import datetime

# 1. Demander la date de naissance à l'utilisateur
date_input = input("Entrez votre date de naissance (DD/MM/YYYY) : ")

# Convertir la chaîne de caractères en objet datetime
birth_date = datetime.strptime(date_input, "%d/%m/%Y")
year = birth_date.year

# Calculer l'âge (Nous sommes en 2026)
today = datetime(2026, 6, 11)
age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

# 2. Déterminer le nombre de bougies (dernier chiffre de l'âge)
# L'opérateur % 10 donne le reste de la division par 10, soit le dernier chiffre
num_candles = age % 10

# Préparer les bougies dynamiquement
# Le gâteau de base a 5 bougies ('iiiii'). On ajuste le visuel.
candles_str = "i" * num_candles
# On centre les bougies pour que le gâteau reste joli
candles_line = f"{candles_str}".center(11, "_")

# Le dessin du gâteau de base personnalisé avec les bougies
cake = f"""
       {candles_line}
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""

# 3. Vérifier si l'année est bissextile (Condition Bonus)
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# 4. Affichage du résultat
print(f"\nVous avez {age} ans. Voici votre gâteau :")

if is_leap_year:
    print("Bonus : Vous êtes né(e) une année bissextile ! Voici deux gâteaux :")
    print(cake)
    print(cake)
else:
    print(cake)