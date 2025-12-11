## Faire avec API et Database, avec FastAPI et SQLAlchemy [A voir plus tard]

## Gestion des clients :
class Client:
    def __init__(self, id: int, nom: str, prenom: str, age: int, permis: str, historique: list["Location"]):
        ## Location via la classe véhicule
        self.id=id
        self.nom=nom
        self.prenom=prenom
        self.age=age
        self.permis=permis
        self.historique=historique
    def __str__(self):
        return f"Client {self.nom} {self.prenom} a {self.age} ans et a un permis {self.permis}"
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

    ## Règles : Age minimum selon le vehicule :
    ## Voiture : 18 ans
    ## Moto : 16 ans
    ## Camion : 18 ans
    def age_minimum_permis_voiture(self):
        return 18
    def age_minimum_permis_moto(self):
        return 16
    def age_minimum_permis_camion(self):
        return 18

    def peut_louer(self, type_vehicule: str, permis_necessaire: str) -> bool:
        """
        Vérifie rapidement si le client est assez âgé et possède le permis demandé.
        type_vehicule peut être 'voiture', 'moto' ou 'camion'
        permis_necessaire correspond au type de permis requis (ex : 'B', 'A', 'C')
    
        Pour interface graphique, faire afficher en liste déroulante pour le permis necessaire, si le client à plusieurs, permis
        SINON, si il a un seul permis, afficher le permis en texte.
        """
        type_vehicule = type_vehicule.lower()
        if type_vehicule == "voiture" and self.age < self.age_minimum_permis_voiture():
            return False
        if type_vehicule == "moto" and self.age < self.age_minimum_permis_moto():
            return False
        if type_vehicule == "camion" and self.age < self.age_minimum_permis_camion():
            return False

        return self.permis.upper() == permis_necessaire.upper()


## Test des fonctions :
# client = Client(1, "Doe", "John", 20, "B", [])
# print(client)
# print(client.age_minimum_permis_voiture())
# print(client.age_minimum_permis_moto())
# print(client.age_minimum_permis_camion())