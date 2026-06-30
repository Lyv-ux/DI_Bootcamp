from googletrans import Translator
french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

translator = Translator()

translations = {}

for word in french_words:
    translated_word = translator.translate(word, src='fr', dest='en').text
    # On l'ajoute au dictionnaire : clé = mot français, valeur = mot anglais
    translations[word] = translated_word

print(translations)