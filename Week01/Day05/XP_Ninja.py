from deep_translator import GoogleTranslator

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

# Initialiser le traducteur (source: français, cible: anglais)
translator = GoogleTranslator(source="fr", target="en")

# Créer le dictionnaire
translated_dict = {
    word: translator.translate(word) for word in french_words
}

print(translated_dict)