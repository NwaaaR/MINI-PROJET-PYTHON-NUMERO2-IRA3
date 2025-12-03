class Vehicule:
    def __init__(self, id, marque, modele, categorie, tarif, etat):
            self.id = id
            self.modele = modele
            self.categorie = categorie
            self.tarif = tarif #Par jour
            self.etat = etat

    def __str__(self):
        return "ID véhicule: " +self.id+", modèle : " +self.modele+", marque : "+self.marque+", categorie : "+self.categorie+", tarif : " +self.tarif+", etat : "+self.etat

    def get_id(self):
         return self.id    

    def get_marque(self):
         return self.get_marque

    def get_modele(self):
         return self.modele 
    
    def get_categorie(self):
         return self.categorie
    
    def get_tarif(self):
         return self.tarif
    
    def get_etat(self):
         return self.etat
         
    def entretien(self,coût):
        self.tarif += coût
        self.etat = "parfait"  