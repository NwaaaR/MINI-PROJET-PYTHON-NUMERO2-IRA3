# tests_systemResa.py
import datetime
from systemResaVoiture import SystemResaVehicule
from voiture import Voiture
import client

systeme = SystemResaVehicule()

cli = client.Client(1, "Test", "User", 25, "B")
systeme.ajouter_client(cli)

car = Voiture(1, "Peugeot", "208", tarif=40.0)
car2 = Voiture(2, "Nissan", "GT-R32", tarif=400.0)
car3 = Voiture(3, "Nissan", "GT-R33", tarif=470.0)
systeme.ajouter_vehicule(car)
systeme.ajouter_vehicule(car2)
systeme.ajouter_vehicule(car3)

debut = datetime.date.today()
fin = debut + datetime.timedelta(days=2)

resa = systeme.creer_reservation(cli, car, debut, fin)

print("Reservation créée:", resa)
print("Chiffre d'affaires:", systeme.rapport_chiffre_affaires())
print("Véhicules disponibles:", systeme.rapport_vehicules_disponibles())