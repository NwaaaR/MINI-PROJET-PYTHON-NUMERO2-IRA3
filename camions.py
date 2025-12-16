import vehicule
class Camion(vehicule.Vehicule):
    # Héritage de Véhicule
    def __init__(self, id: int, marque: str, modele: str, categorie: str = "camion", tarif: float = 0.0, etat: str = "disponible"):
        super().__init__(id, marque, modele, categorie, tarif, etat)
        # super().__init__ est la structure pour initialiser les attributs communs hérité