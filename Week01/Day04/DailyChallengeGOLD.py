import random

class Gene:
    def __init__(self, value=None):
        # Si aucune valeur n'est fournie, on génère aléatoirement 0 ou 1
        self.value = value if value is not None else random.choice([0, 1])

    def mutate(self):
        """Un gène mute en inversant sa valeur (0 devient 1 et inversement)."""
        self.value = 1 - self.value

    def __str__(self):
        return str(self.value)


class Chromosome:
    def __init__(self):
        # Un chromosome est une série de 10 gènes
        self.genes = [Gene() for _ in range(10)]

    def mutate(self, gene_mutation_chance=0.5):
        """Chaque gène a une chance (par défaut 50%) de muter."""
        for gene in self.genes:
            if random.random() < gene_mutation_chance:
                gene.mutate()

    def is_all_ones(self):
        """Vérifie si tous les gènes du chromosome sont à 1."""
        return all(gene.value == 1 for gene in self.genes)

    def __str__(self):
        return "".join(str(gene) for gene in self.genes)


class DNA:
    def __init__(self):
        # Un ADN est une série de 10 chromosomes
        self.chromosomes = [Chromosome() for _ in range(10)]

    def mutate(self, chromosome_mutation_chance=0.5):
        """Chaque chromosome a une chance de muter."""
        for chromosome in self.chromosomes:
            if random.random() < chromosome_mutation_chance:
                chromosome.mutate()

    def is_target_reached(self):
        """L'objectif est atteint si l'ADN n'est composé QUE de 1."""
        return all(chromosome.is_all_ones() for chromosome in self.chromosomes)

    def __str__(self):
        return " | ".join(str(chrom) for chrom in self.chromosomes)


class Organism:
    def __init__(self, dna: DNA, environment_mutation_rate: float):
        self.dna = dna
        # Le taux d'environnement définit la probabilité globale d'activer une mutation
        self.environment_mutation_rate = environment_mutation_rate

    def live_and_mutate(self):
        """L'organisme subit l'influence de son environnement."""
        if random.random() < self.environment_mutation_rate:
            self.dna.mutate()


def run_simulation(population_size=10, env_rate=0.8):
    # Initialisation de la population d'organismes
    population = [Organism(DNA(), env_rate) for _ in range(population_size)]
    
    generations = 0
    success = False
    winner_dna = None

    print(f"🔬 Lancement de la simulation avec {population_size} organismes...")
    print(f"🌍 Impact environnemental (taux de mutation) : {env_rate * 100}%")
    
    # On boucle tant qu'aucun organisme n'a un ADN composé uniquement de 1
    while not success:
        generations += 1
        
        for organism in population:
            organism.live_and_mutate()
            
            if organism.dna.is_target_reached():
                success = True
                winner_dna = organism.dna
                break # On sort de la boucle de la population
                
        # Optionnel : Afficher un indicateur visuel de progression toutes les 50 000 générations
        if generations % 50000 == 0:
            # Compter le nombre max de '1' chez le meilleur individu actuel pour le suivi
            max_ones = max(sum(g.value for c in org.dna.chromosomes for g in c.genes) for org in population)
            print(f"🧬 Génération {generations}... Meilleur score actuel : {max_ones}/100 gènes à 1.")

    return generations, winner_dna

# --- Exécution de l'expérience ---
if __name__ == "__main__":
    generations_needed, final_dna = run_simulation(population_size=20, env_rate=0.7)
    print("\n" + "="*50)
    print("🎯 OBJECTIF ATTEINT !")
    print(f"⏱️  Nombre de générations nécessaires : {generations_needed:,}")
    print(f"🧬 ADN final de l'organisme : {final_dna}")
    print("="*50 + "\n")