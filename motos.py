import vehicule
class Motos(vehicule.Vehicule):
    # Cf infos de camions.py
    def __init__(self, id: int, marque: str, modele: str, categorie: str = "moto", tarif: float = 0.0, etat: str = "disponible"):
        super().__init__(id, marque, modele, categorie, tarif, etat)