import datetime

import streamlit as st

from systemResaVoiture import SystemResaVehicule
from voiture import Voiture
from camions import Camion
from motos import Motos
import client


# ----------------------------------------------------------
# Fonction utilitaire : app.py
# à chaque exécution (Streamlit relance le script à chaque action)
# ----------------------------------------------------------
def creer_systeme_demo() -> SystemResaVehicule:
    systeme = SystemResaVehicule()

    # Création CLI
    cli1 = client.Client(1, "Doe", "John", 22, "B")
    cli2 = client.Client(2, "Marilleau", "Bastien", 30, "B")
    cli3 = client.Client(3, "Marilleau", "Anaelle", 56, "B")
    systeme.ajouter_client(cli1)
    systeme.ajouter_client(cli2)
    systeme.ajouter_client(cli3)

    # Création VOITURE
    v1 = Voiture(1, "Peugeot", "208", tarif=45.0)
    v2 = Voiture(2, "Renault", "Clio", tarif=40.0)
    v3 = Camion(3, "Mercedes", "Actros", tarif=120.0)
    v4 = Motos(4, "Yamaha", "MT-07", tarif=55.0)
    systeme.ajouter_vehicule(v1, v2, v3, v4)

    # LOUÉ
    debut = datetime.date.today()
    fin = debut + datetime.timedelta(days=3)
    systeme.creer_reservation(cli1, v1, debut, fin)

    return systeme


# ----------------------------------------------------------
# Interface Streamlit 
# ----------------------------------------------------------
def main():
    st.title("Location de véhicule")
    st.caption("Interface basé sur du python")

    # ------------------------------------------------------
    # Gestion de l'état : on garde un seul système en mémoire
    # grâce à st.session_state (sinon, tout serait recréé
    # à chaque interaction Streamlit).
    # ------------------------------------------------------
    if "systeme" not in st.session_state:
        st.session_state.systeme = creer_systeme_demo()
    systeme: SystemResaVehicule = st.session_state.systeme

    # Menu simple dans la barre latérale
    vue = st.sidebar.selectbox(
        "Choisir une vue",
        ["Véhicules", "Clients", "Locations", "Statistiques"],
    )

    # ------------------------------------------------------
    # Vue Véhicules
    # ------------------------------------------------------
    if vue == "Véhicules":
        st.header("Véhicules")

        # ---------------------------
        # Formulaire d'ajout de véhicule
        # ---------------------------
        st.subheader("Ajouter un véhicule")
        with st.form("form_nouveau_vehicule"):
            new_vid = len(systeme.vehicules) + 1
            st.write(f"ID (auto) : {new_vid}")
            type_veh = st.selectbox("Type", ["voiture", "moto", "camion"])
            marque = st.text_input("Marque")
            modele = st.text_input("Modèle")
            tarif = st.number_input("Tarif (€/jour)", min_value=0.0, value=40.0, step=1.0)
            submitted_v = st.form_submit_button("Ajouter le véhicule")
        if submitted_v:
            if type_veh == "voiture":
                nv = Voiture(new_vid, marque, modele, tarif=tarif)
            elif type_veh == "moto":
                nv = Motos(new_vid, marque, modele, tarif=tarif)
            else:
                nv = Camion(new_vid, marque, modele, tarif=tarif)
            systeme.ajouter_vehicule(nv)
            st.success(f"Véhicule {marque} {modele} ajouté.")

        # ---------------------------
        # Suppression d'un véhicule
        # ---------------------------
        st.subheader("Supprimer un véhicule")
        vehs_all = systeme.vehicules
        if vehs_all:
            veh_sel = st.selectbox(
                "Choisir un véhicule à supprimer",
                options=vehs_all,
                format_func=lambda v: f"{v.get_id()} - {v.get_marque()} {v.get_modele()} ({v.get_categorie()})",
                key="veh_del",
            )
            if st.button("Supprimer ce véhicule"):
                # On identifie le véhicule par son id pour éviter les soucis d'instance
                vid = veh_sel.get_id()
                # Retirer les réservations associées à ce véhicule
                systeme.reservations = [
                    r for r in systeme.reservations if r.vehicule.get_id() != vid
                ]
                # Nettoyer les listes de véhicules
                systeme.vehicules = [v for v in systeme.vehicules if v.get_id() != vid]
                systeme.voitures = [v for v in systeme.voitures if v.get_id() != vid]
                systeme.camions = [v for v in systeme.camions if v.get_id() != vid]
                systeme.motos = [v for v in systeme.motos if v.get_id() != vid]
                st.success("Véhicule supprimé (et réservations associées).")
        else:
            st.info("Aucun véhicule à supprimer.")

        # Filtre catégorie (None = toutes)
        cat = st.selectbox(
            "Catégorie",
            ["Toutes", "voiture", "moto", "camion"],
            index=0,
        )

        # Filtre dispo uniquement ou non
        seulement_dispo = st.checkbox("Afficher uniquement les véhicules disponibles", value=False)

        if cat == "Toutes":
            vehs = systeme.vehicules
        else:
            vehs = [v for v in systeme.vehicules if v.categorie == cat]

        if seulement_dispo:
            vehs = [v for v in vehs if v.get_etat() == "disponible"]

        # On affiche sous forme de tableau simple
        data = [
            {
                "ID": v.get_id(),
                "Marque": v.get_marque(),
                "Modèle": v.get_modele(),
                "Catégorie": v.get_categorie(),
                "Tarif (€/jour)": v.get_tarif(),
                "État": v.get_etat(),
            }
            for v in vehs
        ]
        st.table(data)

    # ------------------------------------------------------
    # Vue Clients
    # ------------------------------------------------------
    elif vue == "Clients":
        st.header("Clients")

        # ---------------------------
        # Formulaire de création client
        # ---------------------------
        st.subheader("Créer un nouveau client")
        with st.form("form_nouveau_client"):
            # On propose un id simple : taille de la liste + 1
            new_id = len(systeme.rapport_clients()) + 1
            st.write(f"ID (auto) : {new_id}")
            nom = st.text_input("Nom")
            prenom = st.text_input("Prénom")
            age = st.number_input("Âge", min_value=0, max_value=120, value=25, step=1)
            permis = st.selectbox("Type de permis", ["B", "A", "C"])

            submitted = st.form_submit_button("Ajouter le client")

        if submitted:
            # On utilise directement ta classe Client
            nouveau = client.Client(new_id, nom, prenom, int(age), permis)
            systeme.ajouter_client(nouveau)
            st.success(f"Client {nom} {prenom} ajouté.")

        # ---------------------------
        # Suppression simple d'un client
        # ---------------------------
        st.subheader("Supprimer un client")
        clients_actuels = systeme.rapport_clients()
        if clients_actuels:
            client_choisi = st.selectbox(
                "Choisir un client à supprimer",
                options=clients_actuels,
                format_func=lambda c: f"{c.get_id()} - {c.get_nom()} {c.get_prenom()}",
            )
            if st.button("Supprimer ce client"):
                # On supprime aussi ses réservations éventuelles
                systeme.reservations = [
                    r for r in systeme.reservations if r.client != client_choisi
                ]
                # On enlève le client de la liste des clients (par id pour éviter les soucis d'instance)
                systeme.clients = [c for c in systeme.clients if c.get_id() != client_choisi.get_id()]
                st.success("Client supprimé (et ses réservations associées).")
        else:
            st.info("Aucun client à supprimer.")

        st.subheader("Liste des clients")
        data = [
            {
                "ID": c.get_id(),
                "Nom": c.get_nom(),
                "Prénom": c.get_prenom(),
                "Âge": c.get_age(),
                "Permis": c.get_permis(),
                "Nb réservations": len(c.historique),
            }
            for c in systeme.rapport_clients()
        ]
        st.table(data)

    # ------------------------------------------------------
    # Vue Locations
    # ------------------------------------------------------
    elif vue == "Locations":
        st.header("Locations")

        # ---------------------------
        # Créer une nouvelle réservation
        # ---------------------------
        st.subheader("Créer une réservation")
        clients_actuels = systeme.rapport_clients()
        vehicules_dispo = systeme.vehicules_disponibles()

        if not clients_actuels or not vehicules_dispo:
            st.info("Il faut au moins un client et un véhicule disponible.")
        else:
            cli_sel = st.selectbox(
                "Client",
                options=clients_actuels,
                format_func=lambda c: f"{c.get_id()} - {c.get_nom()} {c.get_prenom()}",
                key="loc_client",
            )
            veh_sel = st.selectbox(
                "Véhicule disponible",
                options=vehicules_dispo,
                format_func=lambda v: f"{v.get_id()} - {v.get_marque()} {v.get_modele()} ({v.get_categorie()})",
                key="loc_vehicule",
            )
            col_d1, col_d2 = st.columns(2)
            with col_d1:
                date_debut = st.date_input("Date de début", value=datetime.date.today())
            with col_d2:
                date_fin = st.date_input(
                    "Date de fin",
                    value=datetime.date.today() + datetime.timedelta(days=1),
                )

            if st.button("Créer la réservation"):
                try:
                    systeme.creer_reservation(cli_sel, veh_sel, date_debut, date_fin)
                    st.success("Réservation créée.")
                except Exception as e:
                    st.error(f"Erreur lors de la création : {e}")

        # ---------------------------
        # Afficher et terminer les locations en cours
        # ---------------------------
        st.subheader("Locations en cours")
        locs = systeme.rapport_locations_en_cours()
        if not locs:
            st.info("Aucune location en cours.")
        else:
            # On choisit une réservation à terminer
            resa_sel = st.selectbox(
                "Choisir une réservation à terminer",
                options=locs,
                format_func=lambda r: f"{r.client.nom} {r.client.prenom} -> {r.vehicule.marque} {r.vehicule.modele}",
                key="loc_terminer",
            )
            if st.button("Terminer cette réservation"):
                # On réutilise ta méthode métier : remet le véhicule en disponible,
                # et gère éventuellement les pénalités.
                systeme.terminer_reservation(resa_sel)
                # Puis on enlève vraiment la réservation des listes en se basant
                # sur un "identifiant logique" (client, véhicule, dates, coût),
                # car Streamlit peut recréer les objets entre deux runs.
                key_sel = (
                    resa_sel.client.get_id(),
                    resa_sel.vehicule.get_id(),
                    resa_sel.date_debut,
                    resa_sel.date_fin,
                    resa_sel.cout_total,
                )
                systeme.reservations = [
                    r
                    for r in systeme.reservations
                    if (
                        r.client.get_id(),
                        r.vehicule.get_id(),
                        r.date_debut,
                        r.date_fin,
                        r.cout_total,
                    )
                    != key_sel
                ]
                resa_sel.client.historique = [
                    r
                    for r in resa_sel.client.historique
                    if (
                        r.client.get_id(),
                        r.vehicule.get_id(),
                        r.date_debut,
                        r.date_fin,
                        r.cout_total,
                    )
                    != key_sel
                ]
                st.success("Réservation terminée et supprimée de l'historique.")
                # Petit debug visuel pour vérifier que la suppression est bien prise en compte
                st.write("DEBUG - Nombre total de réservations :", len(systeme.reservations))
                st.write(
                    "DEBUG - Nombre de locations en cours :",
                    len(systeme.rapport_locations_en_cours()),
                )

            # On affiche toujours la liste à jour depuis le système
            locs_aff = systeme.rapport_locations_en_cours()
            data = [
                {
                    "Client": f"{r.client.nom} {r.client.prenom}",
                    "Véhicule": f"{r.vehicule.marque} {r.vehicule.modele}",
                    "Début": r.date_debut,
                    "Fin": r.date_fin,
                    "Coût total (€)": r.cout_total,
                }
                for r in locs_aff
            ]
            st.table(data)

    # ------------------------------------------------------
    # Vue Statistiques
    # ------------------------------------------------------
    elif vue == "Statistiques":
        st.header("Statistiques")
        nb_total = len(systeme.vehicules)
        nb_dispo = len(systeme.vehicules_disponibles())
        nb_clients = len(systeme.rapport_clients())
        ca = systeme.rapport_chiffre_affaires()

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Véhicules en stock", nb_total)
            st.metric("Véhicules disponibles", nb_dispo)
        with col2:
            st.metric("Nombre de clients", nb_clients)
            st.metric("Chiffre d'affaires (€)", ca)


if __name__ == "__main__":
    main()


