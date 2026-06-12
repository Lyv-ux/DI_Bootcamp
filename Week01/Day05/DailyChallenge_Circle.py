import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        """Initialise le cercle soit par son rayon, soit par son diamètre."""
        if radius is not None:
            self.radius = float(radius)
        elif diameter is not None:
            self.diameter = float(diameter)
        else:
            self.radius = 1.0  # Valeur par défaut si rien n'est fourni

    # --- Gestion du Diamètre via les Décorateurs ---
    @property
    def diameter(self):
        """Getter : Calcule le diamètre à partir du rayon."""
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        """Setter : Met à jour le rayon dès que le diamètre change."""
        self.radius = value / 2

    # --- Propriété pour l'Aire ---
    @property
    def area(self):
        """Calcule et retourne l'aire du cercle (pi * r^2)."""
        return math.pi * (self.radius ** 2)

    # --- Dunder Methods (Méthodes Magiques) ---

    def __str__(self):
        """Affichage convivial pour l'utilisateur."""
        return f"Cercle(Rayon: {self.radius:.2f}, Diamètre: {self.diameter:.2f}, Aire: {self.area:.2f})"

    def __repr__(self):
        """Représentation officielle de l'objet (utile dans les listes)."""
        return f"Circle(radius={self.radius})"

    def __add__(self, other):
        """Permet d'additionner deux cercles : c3 = c1 + c2."""
        if not isinstance(other, Circle):
            return NotImplemented
        # On crée un nouveau cercle avec la somme des deux rayons
        return Circle(radius=self.radius + other.radius)

    def __eq__(self, other):
        """Vérifie l'égalité entre deux cercles basée sur le rayon (c1 == c2)."""
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius

    def __lt__(self, other):
        """Inférieur à (c1 < c2). Nécessaire pour pouvoir utiliser sort()."""
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius

    def __gt__(self, other):
        """Supérieur à (c1 > c2)."""
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius