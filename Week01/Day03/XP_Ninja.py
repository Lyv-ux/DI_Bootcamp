class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        # Création de la chaîne décrivant l'appel
        evenement_appel = f"Le numéro {self.phone_number} a appelé le numéro {other_phone.phone_number}."
        print(evenement_appel)
        
        # Ajout à l'historique des appels des DEUX téléphones
        self.call_history.append(evenement_appel)
        other_phone.call_history.append(f"Appel reçu du numéro {self.phone_number}.")

    def show_call_history(self):
        print(f"\n--- Historique des appels pour {self.phone_number} ---")
        if not self.call_history:
            print("Aucun appel dans l'historique.")
        for appel in self.call_history:
            print(f"- {appel}")

    def send_message(self, other_phone, content):
        # Structure du message sous forme de dictionnaire
        message_dict = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        
        # On ajoute le message dans la liste des messages des deux téléphones
        self.messages.append(message_dict)
        other_phone.messages.append(message_dict)
        print(f"Message envoyé de {self.phone_number} à {other_phone.phone_number}.")

    def show_outgoing_messages(self):
        print(f"\n--- Messages ENVOYÉS par {self.phone_number} ---")
        messages_envoyes = [m for m in self.messages if m["from"] == self.phone_number]
        if not messages_envoyes:
            print("Aucun message envoyé.")
        for m in messages_envoyes:
            print(f"À : {m['to']} | Contenu : \"{m['content']}\"")

    def show_incoming_messages(self):
        print(f"\n--- Messages REÇUS par {self.phone_number} ---")
        messages_recus = [m for m in self.messages if m["to"] == self.phone_number]
        if not messages_recus:
            print("Aucun message reçu.")
        for m in messages_recus:
            print(f"De : {m['from']} | Contenu : \"{m['content']}\"")

    def show_messages_from(self, other_phone):
        print(f"\n--- Discussion entre {self.phone_number} et {other_phone.phone_number} ---")
        # On filtre pour afficher l'échange (reçu ou envoyé) avec ce numéro précis
        discussion = [
            m for m in self.messages 
            if (m["from"] == other_phone.phone_number) or (m["to"] == other_phone.phone_number)
        ]
        if not discussion:
            print("Aucun échange avec ce numéro.")
        for m in discussion:
            expediteur = "Moi" if m["from"] == self.phone_number else m["from"]
            print(f"[{expediteur}] : {m['content']}")


# 1. Instanciation de deux objets Phone
mon_tel = Phone("06-12-34-56-78")
tel_ami = Phone("07-98-76-54-32")

print("--- Test des Appels ---")
# 2. Test de la méthode de passage d'appels
mon_tel.call(tel_ami)

# 3. Affichage de l'historique des appels
mon_tel.show_call_history()
tel_ami.show_call_history()

print("\n--- Test des Messages ---")
# 4. Test d'envoi de messages
mon_tel.send_message(tel_ami, "Salut ! Tu vas bien ?")
tel_ami.send_message(mon_tel, "Hello ! Oui et toi ?")
mon_tel.send_message(tel_ami, "Super, merci ! On se voit demain ?")

# 5. Affichage des messages sortants et entrants
mon_tel.show_outgoing_messages()
mon_tel.show_incoming_messages()

# 6. Affichage de la discussion ciblée (Fil de messages)
mon_tel.show_messages_from(tel_ami)