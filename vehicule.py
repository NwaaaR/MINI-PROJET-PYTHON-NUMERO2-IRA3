class Vehicule:
    def __init__(self, id: int, marque: str, modele: str, categorie: str, tarif: float, etat: str = "disponible"):
        # Def ce que tout les véhicule possède
        self.id = id
        self.marque = marque
        self.modele = modele
        self.categorie = categorie
        self.tarif = float(tarif)  # prix par jour
        self.etat = etat  # disponible, loue, maintenance

    def __str__(self):
    # Pour l'affichage
        return f"Vehicule {self.id} | {self.marque} {self.modele} ({self.categorie}) - {self.tarif:.2f}€/jour - {self.etat}"

    def __repr__(self):
        # Cela renvoie une chaîne qui représente l'objet, ex: "Nissan GT-R32 (400.0€/j)"
        return f"{self.marque} {self.modele} ({self.tarif}€/j)"

    def get_id(self):
        return self.id

    def get_marque(self):
        return self.marque

    def get_modele(self):
        return self.modele

    def get_categorie(self):
        return self.categorie

    def get_tarif(self):
        return self.tarif

    def get_etat(self):
        return self.etat

    def set_etat(self, etat: str):
        self.etat = etat

    def entretien(self, cout: float):
        # simple règle : l'entretien remet l'état à parfait et ajuste le coût
        self.tarif += float(cout)
        self.etat = "parfait"