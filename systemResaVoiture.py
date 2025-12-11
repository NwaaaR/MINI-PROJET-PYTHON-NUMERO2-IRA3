import vehicule
import client
import reservation
import camions
import motos
import voiture
import random

class SystemResaVehicule:
    vehicules = []
    voitures = []
    camions = []
    motos = []
    reservations = []
    clients = []
    nb_resa = 0

    def check_resa(date,id):
        for i in range (len(SystemResaVehicule.reservations)):
            if i.id == id and i.date == date:
                return False
        return True    
    
    def reserver(id, date, client):
        coût = random.randint(40, 100)
        if SystemResaVehicule.check_resa(date,id):
            for i in range (len(SystemResaVehicule.vehicules)) :
                if i.id == id:
                    SystemResaVehicule.nb_resa += 1
                    resa = reservation.Reservation(client, i, date, coût,SystemResaVehicule.nb_resa)
                    SystemResaVehicule.reservations.append(resa)
                    return "Votre réservation a bien été enregistrée, le montant s'élève à : " + coût + " €"
        else:
            return "Le véhicule n'est pas disponible sur cette date"        

    def generRapportVehiculeDispo():
        vehiculeDispo = []
        for elt in SystemResaVehicule.vehicules:
            if elt.id not in SystemResaVehicule.reservations :
                vehiculeDispo.append([elt, elt.id])
        return vehiculeDispo        

    def generRapportLoc():
        return SystemResaVehicule.reservations     
    
    def generRapportCA():
        tot = 0 
        for elt in SystemResaVehicule.reservations:
            tot += elt.cout_total 
        return tot      
    
    def affiche_vehicule():
        print(SystemResaVehicule.vehicules)
    


    def main() :
        voiture1 = voiture.Voiture(1, "audi", "a3","berline", 70, "parfait")
        voiture2 = voiture.Voiture(2, "citroën", "xsara Picasso","SUV", 30, "n'en parlons pas")
        voiture3 = voiture.Voiture(3, "peugot", "208","berline", 50, "correct")
        moto1 = motos.Motos(4, "Kawasaki", "Z900", "Roadster", 125, "Neuf")
        moto2 = motos.Motos(5, "Harley-Davidson", "Street Glide", "Cruiser", 93, "Très bien")
        moto3 = motos.Motos(6, "Yamaha", "YZF-R1", "Sportive", 200, "Révision nécessaire")
        camion1 = camions.Camion(7, "Volvo", "FH 500", "Frigorifique", 25, "Parfait")
        camion2 = camions.Camion(8, "Renault Trucks", "T High", "Citerne", 30, "Correct")
        camion3 = camions.Camion(9, "Scania", "R 730", "Plateau", 22, "Vieille mécanique")
        SystemResaVehicule.vehicules.append([voiture1.id,voiture1.marque,voiture1.modele,voiture1.categorie,voiture1.tarif,voiture1.etat])
        SystemResaVehicule.vehicules.append([voiture2.id,voiture2.marque,voiture2.modele,voiture2.categorie,voiture2.tarif,voiture2.etat])
        SystemResaVehicule.vehicules.append([voiture3.id,voiture3.marque,voiture3.modele,voiture3.categorie,voiture3.tarif,voiture3.etat])
        SystemResaVehicule.vehicules.append([moto1.id,moto1.marque,moto1.modele,moto1.categorie,moto1.tarif,moto1.etat])
        SystemResaVehicule.vehicules.append([moto2.id,moto2.marque,moto2.modele,moto2.categorie,moto2.tarif,moto2.etat])
        SystemResaVehicule.vehicules.append([moto3.id,moto3.marque,moto3.modele,moto3.categorie,moto3.tarif,moto3.etat])
        SystemResaVehicule.vehicules.append([camion1.id,camion1.marque,camion1.modele,camion1.categorie,camion1.tarif,camion1.etat])
        SystemResaVehicule.vehicules.append([camion2.id,camion2.marque,camion2.modele,camion2.categorie,camion2.tarif,camion2.etat])
        SystemResaVehicule.vehicules.append([camion3.id,camion3.marque,camion3.modele,camion3.categorie,camion3.tarif,camion3.etat])
        SystemResaVehicule.vehicules.append(voiture2)
        SystemResaVehicule.affiche_vehicule()
        
 
print(SystemResaVehicule.main())
    


