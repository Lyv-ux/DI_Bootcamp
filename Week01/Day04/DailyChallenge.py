import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        """Étape 1 & 2 : Initialisation de la pagination."""
        # Si items est None, on initialise une liste vide
        self.items = items if items is not None else []
        
        # Conversion explicite en entier au cas où
        self.page_size = int(page_size)
        
        # Index de la page actuelle (0-based en interne)
        self.current_idx = 0
        
        # Calcul du nombre total de pages (minimum 1 page, même si vide)
        self.total_pages = max(1, math.ceil(len(self.items) / self.page_size))

    def get_visible_items(self):
        """Étape 3 : Retourne les éléments visibles sur la page actuelle."""
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def getVisibleItems(self):
        """Alias pour correspondre à la syntaxe camelCase du bonus."""
        return self.get_visible_items()

    def go_to_page(self, page_num):
        """Étape 4 : Navigue vers une page spécifique (index utilisateur de 1 à total_pages)."""
        page_num = int(page_num)
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"Page {page_num} hors limites. Le jeu de données contient {self.total_pages} page(s).")
        
        self.current_idx = page_num - 1
        return self

    def first_page(self):
        """Navigue vers la première page."""
        self.current_idx = 0
        return self

    def last_page(self):
        """Navigue vers la dernière page."""
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        """Passe à la page suivante (si possible)."""
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        """Revient à la page précédente (si possible)."""
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    # --- Alias CamelCase pour le chaînage du bonus ---
    def nextPage(self):
        return self.next_page()

    def previousPage(self):
        return self.previous_page()

    def firstPage(self):
        return self.first_page()

    def lastPage(self):
        return self.last_page()

    # --- Étape 5 : Bonus __str__ ---
    def __str__(self):
        """Affiche les éléments de la page actuelle, chacun sur une nouvelle ligne."""
        visible = self.get_visible_items()
        return "\n".join(str(item) for item in visible)


        # Initialisation des données de test
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print("--- Test 1 : Première page ---")
print(p.get_visible_items())  # Output: ['a', 'b', 'c', 'd']

print("\n--- Test 2 : Page suivante ---")
p.next_page()
print(p.get_visible_items())  # Output: ['e', 'f', 'g', 'h']

print("\n--- Test 3 : Dernière page ---")
p.last_page()
print(p.get_visible_items())  # Output: ['y', 'z']

print("\n--- Test 4 : Bonus de la méthode __str__() ---")
p.first_page()
print(str(p))
# Output:
# a
# b
# c
# d

print("\n--- Test 5 : Bonus Méthode Chaining (Chaînage de méthodes) ---")
# On repart de la première page, on avance 3 fois et on récupère les éléments
chained_result = p.firstPage().nextPage().nextPage().nextPage().getVisibleItems()
print(chained_result)  # Output: ['m', 'n', 'o', 'p']

print("\n--- Test 6 : Gestion des erreurs (ValueError) ---")
try:
    p.go_to_page(10)
except ValueError as e:
    print(f"Erreur capturée avec succès : {e}")

try:
    p.go_to_page(0)
except ValueError as e:
    print(f"Erreur capturée avec succès : {e}")