## Faire avec API et Database, avec FastAPI et SQLAlchemy [A voir plus tard]

## Gestion des clients :
class Client:
    def __init__(self, id: int, nom: str, prenom: str, age: int, permis: str, historique=None):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.permis = permis  # type de permis principal (B, A, C)
        self.historique = historique or []

    def __str__(self): # Output format encore
        return f"Client {self.nom} {self.prenom} ({self.age} ans) - permis {self.permis}"

    def get_id(self):
        return self.id

    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def get_age(self):
        return self.age

    def get_permis(self):
        return self.permis
### Règle d'age {IMPORTANT}
    def age_minimum_permis_voiture(self):
        return 18

    def age_minimum_permis_moto(self):
        return 16

    def age_minimum_permis_camion(self):
        return 18
###

### Fonction lié pour voir si la personne peut louer
    def peut_louer(self, type_vehicule: str, permis_necessaire: str) -> bool:
        type_vehicule = type_vehicule.lower()
        if type_vehicule == "voiture" and self.age < self.age_minimum_permis_voiture():
            return False
        if type_vehicule == "moto" and self.age < self.age_minimum_permis_moto():
            return False
        if type_vehicule == "camion" and self.age < self.age_minimum_permis_camion():
            return False
        return self.permis.upper() == permis_necessaire.upper()
        # output booléen -> true ok -> false nop
        # utilisé dans sysrésavehicule.creer_resa
###

    def ajouter_reservation(self, reservation):
        self.historique.append(reservation)