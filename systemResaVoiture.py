import datetime
import vehicule
import client
import reservation
from voiture import Voiture
from camions import Camion
from motos import Motos


class SystemResaVehicule:
    def __init__(self):
        self.vehicules = []
        self.voitures = []
        self.camions = []
        self.motos = []
        self.reservations = []
        self.clients = []

    # Gestion véhicules
    def ajouter_vehicule(self, *vehicules):
            # *vehicule -> arguments variables -> permet d'appeler avec un tuple ici vehicules, contenant les objets passés
        # accepte un ou plusieurs véhicules
        # Principe de l'algo :
        # Add dans la liste général -> add dans la sous liste étant la bonne selon le type de vehicule
        # isinstance verif le type de l'obj
        for veh in vehicules:
            self.vehicules.append(veh)
            if isinstance(veh, Voiture):
                self.voitures.append(veh)
            if isinstance(veh, Camion):
                self.camions.append(veh)
            if isinstance(veh, Motos):
                self.motos.append(veh)

    def vehicules_disponibles(self, categorie=None):
        # 1) On choisit la liste de départ :
        #    - si aucune catégorie n'est précisée -> tous les véhicules
        #    - sinon -> seulement ceux de la catégorie demandée
        if categorie is None:
            liste = self.vehicules
        else:
            liste = []
            for v in self.vehicules:
                if v.categorie == categorie:
                    liste.append(v)

        # 2) On filtre cette liste pour ne garder que les véhicules "disponible"
        disponibles = []
        for v in liste:
            if v.get_etat() == "disponible":
                disponibles.append(v)

        # 3) On renvoie la liste finale de véhicules louables
        return disponibles


    #### Gestion clients
    def ajouter_client(self, cli: client.Client):
        # cli : client.Client -> annotation de type ici "type:hint"
        # dit que cli doit être de la classe Client
        self.clients.append(cli)

    def trouver_client(self, client_id):
        return next((c for c in self.clients if c.id == client_id), None)
    # Recherche par id avec next renvoie le premier client trouver par id, sinon -> None
    ####

    # Réservations
    def creer_reservation(self, cli: client.Client, veh: vehicule.Vehicule, date_debut: datetime.date, date_fin: datetime.date):
        if date_fin <= date_debut:
        # Renvoie de booléen, si le booléen est pas le bon alors on raise
            raise ValueError("Dates invalides")
        if veh.get_etat() != "disponible":
            raise ValueError("Vehicule indisponible")
        if not cli.peut_louer(veh.categorie, self._permis_requis(veh.categorie)):
            raise PermissionError("Client non autorisé")
        cout = self._calculer_cout(veh, date_debut, date_fin)
        resa = reservation.Reservation(cli, veh, date_debut, date_fin, cout)
        self.reservations.append(resa)
        veh.set_etat("loue")
        cli.ajouter_reservation(resa)
        return resa

    def terminer_reservation(self, resa: reservation.Reservation, penalite: float = 0.0):
        if penalite > 0:
            resa.appliquer_penalite(penalite)
        resa.vehicule.set_etat("disponible")

    # Rapport simple
    def rapport_vehicules_disponibles(self):
        return self.vehicules_disponibles()

    def rapport_locations_en_cours(self):
        return [r for r in self.reservations if r.vehicule.get_etat() == "loue"]

    def rapport_chiffre_affaires(self):
        return sum(r.cout_total for r in self.reservations)

    def rapport_clients(self):
        return self.clients

    def rapport_stock(self):
        return self.vehicules

    # Helpers
    def _permis_requis(self, categorie):
        if categorie == "moto":
            return "A"
        if categorie == "camion":
            return "C"
        return "B"

    def _calculer_cout(self, veh: vehicule.Vehicule, date_debut: datetime.date, date_fin: datetime.date):
        jours = (date_fin - date_debut).days
        return veh.get_tarif() * jours