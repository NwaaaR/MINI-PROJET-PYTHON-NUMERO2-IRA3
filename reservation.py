
class Reservation(): 
    def __init__(self, client, vehicule, date, cout_total,id):
        ## Location via la classe véhicule
        self.client = client
        self.vehicule = vehicule
        self.date = date
        self.cout_total = cout_total

        