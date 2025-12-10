import vehicule
import client
import reservation

class SystemResaVehicule:
    vehicules = []
    voitures = []
    camions = []
    motos = []
    reservations = []
    clients = []

    def reserver():
        reservation = 

    def generRapportVehiculeDispo():
        vehiculeDispo = []
        for elt in SystemResaVehicule.vehicules:
            if elt.id not in SystemResaVehicule.reservationsc :
                vehiculeDispo.append(elt)

    def generRapportLoc():
        return SystemResaVehicule.reservations     
    
    def generRapportCA():
        tot = 0 
        for elt in SystemResaVehicule.reservations:
            tot += elt.cout_total 
        return tot    


