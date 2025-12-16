import datetime


class Reservation:
    def __init__(self, client, vehicule, date_debut: datetime.date, date_fin: datetime.date, cout_total: float):
        self.client = client
        self.vehicule = vehicule
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.cout_total = cout_total
        self.penalite = 0.0 # Frais supplementaire sur resa

    def duree(self) -> int: ## Durée de la résa
        return (self.date_fin - self.date_debut).days

    def appliquer_penalite(self, montant: float): ## Ajout péna au coût
        self.penalite += montant
        self.cout_total += montant

    def __str__(self): # format 
        return f"Reservation {self.client.nom} {self.vehicule.modele} du {self.date_debut} au {self.date_fin} - {self.cout_total:.2f}€"
        ## Rappelle :.2f syntax -> nombre float 2 chiffre après virgule

