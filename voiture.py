import vehicule


class Voiture(vehicule.Vehicule):
    def __init__(self, id: int, marque: str, modele: str, categorie: str = "voiture", tarif: float = 0.0, etat: str = "disponible"):
        super().__init__(id, marque, modele, categorie, tarif, etat)